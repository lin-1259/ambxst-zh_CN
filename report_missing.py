#!/usr/bin/env python3
"""Categorize and present missing strings for the user"""
import re, os, json

with open("/root/ambxst-zh_CN/zh_CN.json") as f:
    zh_data = json.load(f)
translated = set()
for items in zh_data.values():
    for item in items:
        if item['chinese']:
            translated.add(item['english'])

with open("/root/ambxst-zh_CN/strings.json") as f:
    strings_data = json.load(f)
all_extracted = set(item['en'] for item in strings_data)
all_already = translated | all_extracted

skip = {
    'HOME', 'USER', 'SEPARATOR', 'SUSPEND', 'WAKE', 'EOSQL', 'PASSWORD',
    'STRINGWHICHHOPEFULLYWONTBEUSED', 'STOP', 'Icon', 'IconButton',
    'Symbols Nerd Font Mono', 'League Gothic', 'Noto Sans', 'Nerd Font',
    'Corner', 'RoundCorner', 'HOME/SEPARATOR', 'Full in ',
    'Display ', 'Device ', 'Battery is at ', 'Idle timer ', '...',
    'Finalizing items with', 'Wrote shader to ', 'Loaded', 'Code',
    'Empty response', 'MMMM yyyy', 'Failed to update icon'}

# Find all QML files
all_qml = []
for root, dirs, files in os.walk('/tmp/Ambxst'):
    for f in files:
        if f.endswith('.qml'):
            all_qml.append(os.path.join(root, f))

dq_pat = re.compile(r'"([A-Z][a-zA-Z0-9 /,.:;\'!?-]{2,100})"')
sq_pat = re.compile(r"'([A-Z][a-zA-Z0-9 /,.:;\"!?-]{2,100})'")

file_map = {}
for fp in all_qml:
    rel = fp.replace('/tmp/Ambxst/', '', 1)
    try:
        with open(fp) as f:
            content = f.read()
    except:
        continue
    
    found = set()
    for m in dq_pat.finditer(content):
        s = m.group(1).strip()
        if s in all_already or s in skip or not s or len(s) < 3:
            continue
        if (s.isupper() or s.isdigit() or re.match(r'^[A-Z0-9_]+$', s) or
            s.startswith('http') or s.startswith('./') or s.startswith('/') or
            s.startswith('{{') or '{{' in s or s.startswith('#')):
            continue
        found.add(s)
    
    for m in sq_pat.finditer(content):
        s = m.group(1).strip()
        if s in all_already or s in skip or not s or len(s) < 3:
            continue
        if s.isupper() or re.match(r'^[A-Z0-9_]+$', s):
            continue
        found.add(s)
    
    if found:
        for s in found:
            if s not in file_map:
                file_map[s] = []
            file_map[s].append(rel)

# Group by category
categories = {
    "🔋 电池/电量": ["Charged", "Charging", "Full", "On battery", "Fully charged",
                     "Critical battery", "Low battery", "Power saver", "Ignore"],
    "⚡ 电源配置": ["Power Save", "Balanced", "Performance", "Active profile"],
    "📌 面板/Dock操作": ["Unpin bar", "Pin bar", "Unpin dock", "Pin dock"],
    "🔒 锁屏": ["Authentication failed"],
    "🌤️ 天气补充": ["Clear sky", "Foggy", "Rime fog", "Evening", "Night"],
    "🎨 壁纸配色方案": ["Content", "Expressive", "Fidelity", "Fruit Salad", "Monochrome",
                      "Neutral", "Rainbow", "Tonal Spot", "Select Scheme"],
    "🖼️ 截图": ["All Screens", "Current Screen", "Failed to parse monitors",
                  "Failed to fetch monitors", "Failed to save image"],
    "🎬 录屏": ["Screen Recorder", "Screen Recorder Error", "Recording saved to "],
    "🔇 音频": ["Unmute", "Mute", "Volume protection active", "Volume jump limited"],
    "📋 剪贴板": ["No selection", "Failed to parse response", "Failed to fetch preview"],
    "🎵 音乐播放器": ["Nothing Playing", "Enjoy the silence", "Unknown Player"],
    "⬆️ 更新服务": ["Ambxst Update", "Maybe later"],
    "📁 预设管理": ["Cannot load empty preset name", "Cannot save preset with empty name",
                    "No config files selected for preset", "Cannot rename official preset",
                    "Cannot rename to official name", "Invalid rename parameters"],
    "🔘 按钮标签": ["Open Launcher", "Open Window Overview", "Power Menu",
                    "Open Presets Manager", "Search windows..."],
    "🛠️ 其他": ["Bypassed", "Pomodoro", "Edit with Gradia"],
    # Already in zh_CN.json but from different files
    "✅ 已翻译（重复）": ["Tools", "Lock Session", "Suspend", "Hibernate",
                         "Exit AxctlService", "Reboot", "Power Off"],
}

print("=" * 60)
print("  Ambxst 遗漏字符串检查报告")
print("=" * 60)

all_strings = set()
for cat, strs in categories.items():
    for s in strs:
        all_strings.add(s)

total_new = 0
for cat, strs in categories.items():
    is_new = cat != "✅ 已翻译（重复）"
    if is_new:
        total_new += len(strs)
    print(f"\n{cat} ({len(strs)} 条{'，含已翻译' if not is_new else ''}):")
    for s in strs:
        sources = file_map.get(s, ["???"])
        print(f'    "{s}"')
        for src in sources[:2]:
            print(f'      📍 {src}')

print(f"\n{'=' * 60}")
print(f"新增待翻译: {total_new} 条")
print(f"需人工确认: Material You 配色方案名称是否保留英文")
print(f"{'=' * 60}")