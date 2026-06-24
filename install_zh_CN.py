#!/usr/bin/env python3
"""
Ambxst Shell 中文汉化安装脚本
读取 zh_CN.json，将 Ambxst QML 源码中的英文替换为中文

用法:
    python3 install_zh_CN.py            # 汉化
    python3 install_zh_CN.py --revert   # 恢复英文（如有备份）
"""

import json
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ZH_CN_JSON = os.path.join(SCRIPT_DIR, "zh_CN.json")

# 可能的 Ambxst 源码位置
SEARCH_PATHS = [
    os.path.expanduser("~/.local/share/ambxst"),
    os.path.expanduser("~/ambxst"),
    "/usr/local/share/ambxst",
    "/opt/ambxst",
    "/tmp/ambxst",
]

def find_ambxst_dir():
    """找到 Ambxst 源码目录"""
    for p in SEARCH_PATHS:
        modules_dir = os.path.join(p, "modules")
        if os.path.isdir(modules_dir):
            return p
    return None

def find_qml_file(ambxst_dir, module_key):
    """
    根据模块键名找到对应的 QML 文件路径
    例如: modules_bar_clock_Clock -> ambxst_dir/modules/bar/clock/Clock.qml
    """
    # 移除 modules_ 前缀
    rel_path = module_key
    if rel_path.startswith("modules_"):
        rel_path = rel_path[8:]  # len("modules_")
    if rel_path.startswith("_"):
        rel_path = rel_path[1:]
    
    # 用 / 替换 _
    rel_path = rel_path.replace("_", "/") + ".qml"
    
    full_path = os.path.join(ambxst_dir, rel_path)
    # 检查是否存在
    if os.path.isfile(full_path):
        return full_path
    
    # 也试试 modules/ 前缀
    alt_path = os.path.join(ambxst_dir, "modules", rel_path.lstrip("modules/"))
    if os.path.isfile(alt_path):
        return alt_path
    
    return None

def backup_file(filepath):
    """备份原始文件"""
    backup = filepath + ".bak"
    if not os.path.isfile(backup):
        shutil.copy2(filepath, backup)
        return True
    return False

def patch_file(filepath, replacements):
    """
    在 QML 文件中进行字符串替换
    replacements: [(old_string, new_string), ...]
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def revert_file(filepath):
    """恢复备份"""
    backup = filepath + ".bak"
    if os.path.isfile(backup):
        shutil.copy2(backup, filepath)
        os.remove(backup)
        return True
    return False

def main():
    revert_mode = "--revert" in sys.argv

    # 加载翻译
    if not os.path.isfile(ZH_CN_JSON):
        print(f"[ERROR] 找不到翻译文件: {ZH_CN_JSON}")
        sys.exit(1)
    
    with open(ZH_CN_JSON, 'r', encoding='utf-8') as f:
        translations = json.load(f)

    # 找到 Ambxst 目录
    ambxst_dir = find_ambxst_dir()
    if not ambxst_dir:
        print("[ERROR] 找不到 Ambxst 安装目录！")
        print(f"  请确认 Ambxst 已安装，或手动修改脚本中的 SEARCH_PATHS")
        sys.exit(1)
    print(f"✅ 找到 Ambxst: {ambxst_dir}")

    # 提取翻译映射: {file_key: {en: zh}}
    file_translations = {}
    for key, value in translations.items():
        if key.startswith("_"):  # 跳过注释
            continue
        if isinstance(value, dict):
            file_translations[key] = value

    patched_count = 0
    total_replacements = 0

    for module_key, string_map in file_translations.items():
        qml_path = find_qml_file(ambxst_dir, module_key)
        if not qml_path:
            # 尝试一些可能的路径变体
            print(f"  ⚠️  找不到文件: {module_key}")
            continue

        # 过滤出有翻译的
        replacements = [(en, zh) for en, zh in string_map.items() if zh.strip()]
        if not replacements:
            continue

        if revert_mode:
            if revert_file(qml_path):
                print(f"  🔄 已恢复: {qml_path}")
            continue

        # 备份并替换
        backup_file(qml_path)
        success = patch_file(qml_path, replacements)
        if success:
            total_replacements += len(replacements)
            patched_count += 1
            print(f"  ✅ {len(replacements):3d} 处  → {qml_path}")
        else:
            print(f"  -  无变化: {qml_path}")

    # 输出结果
    if revert_mode:
        print(f"\n✅ 已恢复 {patched_count} 个文件")
    else:
        print(f"\n✅ 汉化完成！共 {patched_count} 个文件，{total_replacements} 处替换")
        print("  请重启 Ambxst 以生效: ambxst & disown")
        print("  如需恢复英文: python3 install_zh_CN.py --revert")


if __name__ == "__main__":
    main()
