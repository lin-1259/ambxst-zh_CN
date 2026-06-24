#!/usr/bin/env python3
"""Scan all QML files for untranslated strings"""
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

# Build set of all strings already in strings.json (regardless of translation status)
# Also check strings_flat.json
import glob
all_already = translated | all_extracted
sf_path = "/root/ambxst-zh_CN/strings_flat.json"
if os.path.exists(sf_path):
    with open(sf_path) as f:
        sf_data = json.load(f)
    for item in sf_data:
        all_already.add(item.get('en', ''))

# Skip list for internal identifiers
skip = {'HOME', 'USER', 'SEPARATOR', 'SUSPEND', 'WAKE', 'EOSQL', 'PASSWORD',
        'STRINGWHICHHOPEFULLYWONTBEUSED', 'STOP', 'Icon', 'IconButton',
        'Symbols Nerd Font Mono', 'League Gothic', 'Noto Sans', 'Nerd Font',
        'Corner', 'RoundCorner', 'HOME/SEPARATOR', 'Full in ',
        'Display ', 'Device ', 'Battery is at ', 'Idle timer ', '...',
        'Screenshot', 'Finalizing items with', 'Wrote shader to ',
        'Loaded', 'Code', 'Empty response', 'MMMM yyyy', 'Corner',
        'RoundCorner', 'SUSPEND', 'WAKE', 'Failed to update icon',
        'Failed to fetch monitors'}

# Find all QML files
all_qml = []
for root, dirs, files in os.walk('/tmp/Ambxst'):
    for f in files:
        if f.endswith('.qml'):
            all_qml.append(os.path.join(root, f))

# Pattern for quoted strings that look like English UI text
# Match "Word word..." or 'Word word...'
dq_pat = re.compile(r'"([A-Z][a-zA-Z0-9 /,.:;\'!?-]{2,100})"')
sq_pat = re.compile(r"'([A-Z][a-zA-Z0-9 /,.:;\"!?-]{2,100})'")

candidates = {}
for fp in all_qml:
    rel = fp.replace('/tmp/Ambxst/', '', 1)
    try:
        with open(fp) as f:
            content = f.read()
    except:
        continue
    
    found = set()
    
    # Double-quoted
    for m in dq_pat.finditer(content):
        s = m.group(1).strip()
        if s in all_already or s in skip:
            continue
        if not s or len(s) < 3:
            continue
        if (s.isupper() or s.isdigit() or 
            re.match(r'^[A-Z0-9_]+$', s) or
            s.startswith('http') or s.startswith('./') or s.startswith('/') or
            s.startswith('{{') or '{{' in s or
            s.startswith('#')):
            continue
        # Filter out obvious non-UI strings (file paths, URLs, etc)
        if '.' in s and s.count('.') > 1 and '/' not in s:
            continue
        found.add(s)
    
    # Single-quoted
    for m in sq_pat.finditer(content):
        s = m.group(1).strip()
        if s in all_already or s in skip:
            continue
        if not s or len(s) < 3:
            continue
        if (s.isupper() or re.match(r'^[A-Z0-9_]+$', s)):
            continue
        found.add(s)
    
    if found:
        candidates[rel] = sorted(found)

print(f"发现 {len(candidates)} 个文件包含未翻译的新字符串")
total = sum(len(v) for v in candidates.values())
print(f"总计约 {total} 条候选字符串\n")

for qml, strs in sorted(candidates.items()):
    print(f"[{qml}]")
    for s in strs:
        print(f'  "{s}"')
    print()