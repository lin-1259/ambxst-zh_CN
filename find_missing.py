#!/usr/bin/env python3
"""Find QML strings not captured in strings.json"""
import re, os, json

STRINGS_JSON = "/root/ambxst-zh_CN/strings.json"
ZH_CN_JSON = "/root/ambxst-zh_CN/zh_CN.json"
ALL_QML = "/tmp/all_qml.txt"
AMBXST_DIR = "/tmp/Ambxst"

with open(STRINGS_JSON) as f:
    data = json.load(f)
files_in_json = set(item['f'] for item in data)

with open(ZH_CN_JSON) as f:
    zh_data = json.load(f)
already_translated = set()
for items in zh_data.values():
    for item in items:
        if item['chinese']:
            already_translated.add(item['english'])

with open(ALL_QML) as f:
    all_qml = [line.strip().lstrip('./') for line in f if line.strip()]

not_in_json = []
for qml in all_qml:
    found = False
    for fj in files_in_json:
        if qml == fj or fj.endswith(qml):
            found = True; break
    if not found:
        not_in_json.append(qml)

skip_set = {'HOME', 'USER', 'SEPARATOR', 'SUSPEND', 'WAKE', 'EOSQL', 'PASSWORD',
            'STRINGWHICHHOPEFULLYWONTBEUSED', 'STOP', 'Icon', 'IconButton',
            'Symbols Nerd Font Mono', 'League Gothic', 'Noto Sans', 'Nerd Font',
            'Corner', 'RoundCorner', 'HOME/SEPARATOR', 'Full in ',
            'Display ', 'Device ', 'Battery is at ', 'Idle timer ', '...',
            'Screenshot', 'Finalizing items with', 'Wrote shader to ',
            'Failed to fetch monitors', 'Failed to update icon',
            'Loaded', 'Code', 'Empty response', 'MMMM yyyy'}

new_strings = {}
for qml in not_in_json:
    filepath = os.path.join(AMBXST_DIR, qml)
    if not os.path.exists(filepath):
        continue
    with open(filepath) as f:
        content = f.read()
    
    found = set()
    # Find double-quoted strings that look like UI text
    for m in re.finditer(r'text:\s*"([^"]{3,})"', content):
        s = m.group(1).strip()
        if s not in skip_set and s not in already_translated and not s.isupper():
            found.add(s)
    
    for m in re.finditer(r'label:\s*"([^"]{3,})"', content):
        s = m.group(1).strip()
        if s not in skip_set and s not in already_translated and not s.isupper():
            found.add(s)
    
    for m in re.finditer(r'placeholderText:\s*"([^"]{3,})"', content):
        s = m.group(1).strip()
        if s not in skip_set and s not in already_translated:
            found.add(s)
    
    for m in re.finditer(r'(title|tooltip|heading|message|hint|subtitle|caption|warning|errorMessage)\s*:\s*"([^"]{3,})"', content):
        s = m.group(2).strip()
        if s not in skip_set and s not in already_translated and not s.isupper():
            found.add(s)
    
    for m in re.finditer(r'(displayText|buttonText|emptyText|noMatchesText)\s*:\s*"([^"]{3,})"', content):
        s = m.group(2).strip()
        if s not in skip_set and s not in already_translated:
            found.add(s)
    
    # qsTr calls
    for m in re.finditer(r'qsTr\("([^"]{3,})"\)', content):
        s = m.group(1).strip()
        if s not in skip_set and s not in already_translated and not s.isupper():
            found.add(s)
    
    # Single-quoted UI strings (common in QML)
    for m in re.finditer(r"(?::|,)\s*'([A-Z][a-zA-Z0-9 ,]{3,60})'", content):
        s = m.group(1).strip()
        if s in skip_set or s in already_translated or s.isupper():
            continue
        if re.match(r'^[A-Z0-9_]{3,}$', s):
            continue
        found.add(s)
    
    if found:
        new_strings[qml] = sorted(found)

print("=== 遗漏的新 UI 字符串 ===")
total = 0
for qml, strs in sorted(new_strings.items()):
    total += len(strs)
    print(f"\n--- {qml} ---")
    for s in strs:
        print(f'  "{s}"')

print(f"\n\n总计: {len(new_strings)} 个文件, {total} 条新字符串")
