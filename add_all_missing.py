#!/usr/bin/env python3
"""Add all 66 missing strings directly to strings.json and zh_CN.json"""
import json

STRINGS_FILE = "/root/ambxst-zh_CN/strings.json"
ZH_CN_FILE = "/root/ambxst-zh_CN/zh_CN.json"

with open(STRINGS_FILE) as f:
    strings = json.load(f)

with open(ZH_CN_FILE) as f:
    zh_data = json.load(f)

# All translations for the 66 new strings
translations = {
    # Battery indicator
    "Charged": "已充满",
    "Charging": "充电中",
    "Full": "已满",
    "On battery": "使用电池中",
    "Fully charged": "已充满",
    # Battery service
    "Critical battery": "电池电量极低",
    "Low battery": "电池电量低",
    "Power saver": "省电模式",
    "Ignore": "忽略",
    # Power Profile
    "Power Save": "省电",
    "Balanced": "平衡",
    "Performance": "性能",
    "Active profile": "当前配置",
    # Dock/Bar
    "Unpin bar": "取消固定面板",
    "Pin bar": "固定面板",
    "Unpin dock": "取消固定 Dock",
    "Pin dock": "固定 Dock",
    # Lockscreen
    "Authentication failed": "认证失败",
    # Weather
    "Clear sky": "晴朗",
    "Foggy": "有雾",
    "Rime fog": "雾凇",
    "Evening": "傍晚",
    "Night": "夜间",
    # Wallpaper scheme (Material You)
    "Content": "内容",
    "Expressive": "表现力",
    "Fidelity": "保真",
    "Fruit Salad": "水果沙拉",
    "Monochrome": "单色",
    "Neutral": "中性",
    "Rainbow": "彩虹",
    "Tonal Spot": "色调聚点",
    "Select Scheme": "选择方案",
    # Screenshot
    "All Screens": "所有屏幕",
    "Current Screen": "当前屏幕",
    "Failed to parse monitors": "解析显示器失败",
    "Failed to fetch monitors": "获取显示器失败",
    "Failed to save image": "保存图片失败",
    # Screen Recorder
    "Screen Recorder": "屏幕录制",
    "Screen Recorder Error": "屏幕录制错误",
    "Recording saved to ": "录制已保存到 ",
    # Audio
    "Unmute": "取消静音",
    "Mute": "静音",
    "Volume protection active": "音量保护已激活",
    "Volume jump limited": "音量跳跃受限",
    # Clipboard
    "No selection": "未选择",
    "Failed to parse response": "响应解析失败",
    "Failed to fetch preview": "预览获取失败",
    # Player
    "Nothing Playing": "无播放内容",
    "Enjoy the silence": "享受寂静",
    "Unknown Player": "未知播放器",
    # Update
    "Ambxst Update": "Ambxst 更新",
    "Maybe later": "稍后再说",
    # Presets
    "Cannot load empty preset name": "无法加载空的预设名称",
    "Cannot save preset with empty name": "无法保存空的预设名称",
    "No config files selected for preset": "未为预设选择配置文件",
    "Cannot rename official preset": "无法重命名官方预设",
    "Cannot rename to official name": "无法重命名为官方名称",
    "Invalid rename parameters": "无效的重命名参数",
    # Buttons
    "Open Launcher": "打开启动器",
    "Open Window Overview": "打开窗口概览",
    "Power Menu": "电源菜单",
    "Open Presets Manager": "打开预设管理器",
    "Search windows...": "搜索窗口...",
    # Other
    "Bypassed": "已绕过",
    "Pomodoro": "番茄钟",
    "Edit with Gradia": "用 Gradia 编辑",
}

# New entries with their file paths and properties
new_entries = [
    # Battery indicator
    {"f": "modules/bar/BatteryIndicator.qml", "p": "text", "en": "Charged"},
    {"f": "modules/bar/BatteryIndicator.qml", "p": "text", "en": "Charging"},
    {"f": "modules/bar/BatteryIndicator.qml", "p": "text", "en": "Full"},
    {"f": "modules/bar/BatteryIndicator.qml", "p": "text", "en": "On battery"},
    {"f": "modules/bar/BatteryIndicator.qml", "p": "text", "en": "Fully charged"},
    # Battery service (notification messages)
    {"f": "modules/services/Battery.qml", "p": "text", "en": "Critical battery"},
    {"f": "modules/services/Battery.qml", "p": "text", "en": "Low battery"},
    {"f": "modules/services/Battery.qml", "p": "text", "en": "Power saver"},
    {"f": "modules/services/Battery.qml", "p": "text", "en": "Ignore"},
    # Power Profile
    {"f": "modules/services/PowerProfile.qml", "p": "text", "en": "Power Save"},
    {"f": "modules/services/PowerProfile.qml", "p": "text", "en": "Balanced"},
    {"f": "modules/services/PowerProfile.qml", "p": "text", "en": "Performance"},
    {"f": "modules/services/PowerProfile.qml", "p": "text", "en": "Active profile"},
    # Bar content
    {"f": "modules/bar/BarContent.qml", "p": "text", "en": "Unpin bar"},
    {"f": "modules/bar/BarContent.qml", "p": "text", "en": "Pin bar"},
    # Dock content
    {"f": "modules/dock/DockContent.qml", "p": "text", "en": "Unpin dock"},
    {"f": "modules/dock/DockContent.qml", "p": "text", "en": "Pin dock"},
    # Lockscreen
    {"f": "modules/lockscreen/LockScreen.qml", "p": "text", "en": "Authentication failed"},
    # Weather
    {"f": "modules/services/WeatherService.qml", "p": "text", "en": "Clear sky"},
    {"f": "modules/services/WeatherService.qml", "p": "text", "en": "Foggy"},
    {"f": "modules/services/WeatherService.qml", "p": "text", "en": "Rime fog"},
    {"f": "modules/services/WeatherService.qml", "p": "text", "en": "Evening"},
    {"f": "modules/services/WeatherService.qml", "p": "text", "en": "Night"},
    # Wallpaper scheme selector
    {"f": "modules/widgets/dashboard/wallpapers/SchemeSelector.qml", "p": "text", "en": "Content"},
    {"f": "modules/widgets/dashboard/wallpapers/SchemeSelector.qml", "p": "text", "en": "Expressive"},
    {"f": "modules/widgets/dashboard/wallpapers/SchemeSelector.qml", "p": "text", "en": "Fidelity"},
    {"f": "modules/widgets/dashboard/wallpapers/SchemeSelector.qml", "p": "text", "en": "Fruit Salad"},
    {"f": "modules/widgets/dashboard/wallpapers/SchemeSelector.qml", "p": "text", "en": "Monochrome"},
    {"f": "modules/widgets/dashboard/wallpapers/SchemeSelector.qml", "p": "text", "en": "Neutral"},
    {"f": "modules/widgets/dashboard/wallpapers/SchemeSelector.qml", "p": "text", "en": "Rainbow"},
    {"f": "modules/widgets/dashboard/wallpapers/SchemeSelector.qml", "p": "text", "en": "Tonal Spot"},
    {"f": "modules/widgets/dashboard/wallpapers/SchemeSelector.qml", "p": "text", "en": "Select Scheme"},
    # Screenshot service
    {"f": "modules/services/Screenshot.qml", "p": "text", "en": "All Screens"},
    {"f": "modules/services/Screenshot.qml", "p": "text", "en": "Current Screen"},
    {"f": "modules/services/Screenshot.qml", "p": "text", "en": "Failed to parse monitors"},
    {"f": "modules/services/Screenshot.qml", "p": "text", "en": "Failed to fetch monitors"},
    {"f": "modules/services/Screenshot.qml", "p": "text", "en": "Failed to save image"},
    # Screen Recorder
    {"f": "modules/services/ScreenRecorder.qml", "p": "text", "en": "Screen Recorder"},
    {"f": "modules/services/ScreenRecorder.qml", "p": "text", "en": "Screen Recorder Error"},
    {"f": "modules/services/ScreenRecorder.qml", "p": "text", "en": "Recording saved to "},
    # Audio
    {"f": "modules/widgets/dashboard/controls/AudioVolumeEntry.qml", "p": "text", "en": "Unmute"},
    {"f": "modules/widgets/dashboard/controls/AudioVolumeEntry.qml", "p": "text", "en": "Mute"},
    {"f": "modules/widgets/dashboard/controls/AudioVolumeEntry.qml", "p": "text", "en": "Volume protection active"},
    {"f": "modules/services/Audio.qml", "p": "text", "en": "Volume jump limited"},
    # Clipboard
    {"f": "modules/services/ClipboardService.qml", "p": "text", "en": "No selection"},
    {"f": "modules/services/ClipboardService.qml", "p": "text", "en": "Failed to parse response"},
    {"f": "modules/services/ClipboardService.qml", "p": "text", "en": "Failed to fetch preview"},
    # Player
    {"f": "modules/widgets/dashboard/widgets/FullPlayer.qml", "p": "text", "en": "Nothing Playing"},
    {"f": "modules/widgets/dashboard/widgets/FullPlayer.qml", "p": "text", "en": "Enjoy the silence"},
    {"f": "modules/widgets/dashboard/widgets/FullPlayer.qml", "p": "text", "en": "Unknown Player"},
    # Update
    {"f": "modules/services/UpdateService.qml", "p": "text", "en": "Ambxst Update"},
    {"f": "modules/services/UpdateService.qml", "p": "text", "en": "Maybe later"},
    # Presets
    {"f": "modules/services/PresetsService.qml", "p": "text", "en": "Cannot load empty preset name"},
    {"f": "modules/services/PresetsService.qml", "p": "text", "en": "Cannot save preset with empty name"},
    {"f": "modules/services/PresetsService.qml", "p": "text", "en": "No config files selected for preset"},
    {"f": "modules/services/PresetsService.qml", "p": "text", "en": "Cannot rename official preset"},
    {"f": "modules/services/PresetsService.qml", "p": "text", "en": "Cannot rename to official name"},
    {"f": "modules/services/PresetsService.qml", "p": "text", "en": "Invalid rename parameters"},
    # Buttons
    {"f": "modules/widgets/dashboard/LauncherButton.qml", "p": "text", "en": "Open Launcher"},
    {"f": "modules/widgets/overview/OverviewButton.qml", "p": "text", "en": "Open Window Overview"},
    {"f": "modules/widgets/powermenu/PowerButton.qml", "p": "text", "en": "Power Menu"},
    {"f": "modules/widgets/presets/PresetsButton.qml", "p": "text", "en": "Open Presets Manager"},
    {"f": "modules/widgets/overview/OverviewPopup.qml", "p": "placeholderText", "en": "Search windows..."},
    # Other
    {"f": "modules/widgets/dashboard/controls/PanelTitlebar.qml", "p": "text", "en": "Bypassed"},
    {"f": "modules/bar/clock/Pomodoro.qml", "p": "text", "en": "Pomodoro"},
    {"f": "modules/tools/ScreenshotOverlay.qml", "p": "text", "en": "Edit with Gradia"},
]

# Add to strings.json
existing_keys = {(item['f'], item['p'], item['en']) for item in strings}
new_count = 0
for entry in new_entries:
    key = (entry['f'], entry['p'], entry['en'])
    if key not in existing_keys:
        strings.append(entry)
        existing_keys.add(key)
        new_count += 1

# Write updated strings.json
with open(STRINGS_FILE, 'w', encoding='utf-8') as f:
    json.dump(strings, f, ensure_ascii=False, indent=2)
print(f"strings.json: 新增 {new_count} 条")

# Update zh_CN.json
zh_new_count = 0
for entry in new_entries:
    fp = entry['f']
    cn = translations.get(entry['en'], "")
    if not cn:
        print(f"  跳过未翻译: {entry['en']}")
        continue
    
    item = {
        "property": entry['p'],
        "english": entry['en'],
        "chinese": cn
    }
    
    if fp not in zh_data:
        zh_data[fp] = [item]
        zh_new_count += 1
    else:
        # Check for duplicate
        dup = False
        for existing in zh_data[fp]:
            if existing['property'] == entry['p'] and existing['english'] == entry['en']:
                dup = True
                break
        if not dup:
            zh_data[fp].append(item)
            zh_new_count += 1

with open(ZH_CN_FILE, 'w', encoding='utf-8') as f:
    json.dump(zh_data, f, ensure_ascii=False, indent=2)
print(f"zh_CN.json: 新增 {zh_new_count} 条")

# Final stats
total = sum(len(v) for v in zh_data.values())
filled = sum(1 for v in zh_data.values() for item in v if item['chinese'])
print(f"\n最终统计:")
print(f"  strings.json: {len(strings)} 条")
print(f"  zh_CN.json: {total} 条, 已翻译 {filled} 条")
print(f"  覆盖文件: {len(zh_data)} 个")