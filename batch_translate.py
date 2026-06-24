#!/usr/bin/env python3
"""批量翻译 Ambxst 汉化文件"""
import json
from pathlib import Path

STRINGS_FILE = Path("/root/ambxst-zh_CN/strings.json")
ZH_CN_FILE = Path("/root/ambxst-zh_CN/zh_CN.json")

# 翻译字典 - 精简版，只翻译关键UI字符串
translations = {
    # 基础控件
    "Background": "背景",
    "Popup": "弹出窗口",
    "Internal BG": "内部背景",
    "Bar BG": "面板背景",
    "Pane": "窗格",
    "Common": "通用",
    "Focus": "焦点",
    "Primary": "主色",
    "Primary Focus": "主色焦点",
    "Over Primary": "覆盖主色",
    "Secondary": "次要色",
    "Secondary Focus": "次要焦点",
    "Over Secondary": "覆盖次要色",
    "Tertiary": "第三色",
    "Tertiary Focus": "第三焦点",
    "Over Tertiary": "覆盖第三色",
    "Error": "错误",
    "Error Focus": "错误焦点",
    "Over Error": "覆盖错误",
    
    # 工具菜单
    "Screenshot": "截图",
    "Open Screenshots": "打开截图",
    "Open Recordings": "打开录制",
    "Color Picker": "取色器",
    "QR Code": "二维码",
    "Google Lens": "Google 镜头",
    "Mirror": "镜像",
    
    # 设置窗口
    "Ambxst Settings": "Ambxst 设置",
    
    # AI 面板
    "AI & API Keys": "AI 与 API 密钥",
    "Enter API Key...": "输入 API 密钥...",
    "Custom Provider": "自定义提供商",
    "Custom Provider API Key": "自定义提供商 API 密钥",
    "Save": "保存",
    "Clear": "清除",
    "Custom Endpoint": "自定义端点",
    "Custom cURL Template": "自定义 cURL 模板",
    
    # 通知
    "Notifications": "通知",
    
    # tmux
    "Search or create tmux session...": "搜索或创建 tmux 会话...",
    "Open": "打开",
    "Rename": "重命名",
    "Quit": "退出",
    "No panes to display": "无可显示的窗格",
    "Loading panes...": "加载窗格中...",
    "No session selected": "未选择会话",
    "Select a session to preview": "选择一个会话预览",
    
    # 剪贴板
    "Search in clipboard...": "在剪贴板中搜索...",
    "Clear all?": "清除全部?",
    "Copy": "复制",
    "Alias": "别名",
    "Delete": "删除",
    "No clipboard history": "无剪贴板历史记录",
    "Copy something to get started": "复制一些内容开始使用",
    "Loading preview...": "加载预览中...",
    "Link": "链接",
    "MIME Type": "MIME 类型",
    "Size": "大小",
    "Date": "日期",
    "Checksum": "校验和",
    
    # 颜色选择器
    "Custom": "自定义",
    "Color picker": "取色器",
    "Enter password...": "输入密码...",
    
    # 主题面板
    "Discard changes": "丢弃更改",
    "Apply changes": "应用更改",
    "Back": "返回",
    "General": "常规",
    "Shadow": "阴影",
    "Colors": "颜色",
    "Wallpapers": "壁纸",
    "Default": "默认",
    "Tint Icons": "图标着色",
    "Enable Corners": "启用圆角",
    "Animation": "动画",
    "Fonts": "字体",
    "UI Font": "UI 字体",
    "Mono Font": "等宽字体",
    "Roundness": "圆角程度",
    "Opacity": "透明度",
    "Blur": "模糊",
    "Offset X": "X 偏移",
    "Offset Y": "Y 偏移",
    "Color": "颜色",
    "Variant": "变体",
    "Editor - ": "编辑器 - ",
    "Open color picker": "打开取色器",
    "Select Color": "选择颜色",
    
    # 变体编辑器
    "Item Color": "项目颜色",
    "Border": "边框",
    "Angle": "角度",
    "Dot Color": "点颜色",
    "Background": "背景",
    "Range": "范围",
    
    # 音频混音器
    "Sound": "声音",
    "Open PipeWire Volume Control": "打开 PipeWire 音量控制",
    "Output": "输出",
    "Input": "输入",
    "Volume": "音量",
    "Balance": "平衡",
}

# 加载原始数据
with open(STRINGS_FILE) as f:
    original_data = json.load(f)

# 构建 zh_CN.json
zh_cn_data = {}
empty_count = 0
translated_count = 0

for item in original_data:
    file_path = item['f']
    prop = item['p']
    en_text = item['en']
    
    # 查找翻译
    cn_text = translations.get(en_text, "")
    
    if cn_text:
        translated_count += 1
    else:
        empty_count += 1
    
    # 按文件分组
    if file_path not in zh_cn_data:
        zh_cn_data[file_path] = []
    
    zh_cn_data[file_path].append({
        "property": prop,
        "english": en_text,
        "chinese": cn_text
    })

# 保存
with open(ZH_CN_FILE, 'w', encoding='utf-8') as f:
    json.dump(zh_cn_data, f, ensure_ascii=False, indent=2)

print(f"翻译完成!")
print(f"  已翻译: {translated_count} 条")
print(f"  待翻译: {empty_count} 条")
print(f"  总计: {len(original_data)} 条")

# 输出未翻译的
if empty_count > 0:
    print("\n未翻译的字符串:")
    for item in original_data:
        en_text = item['en']
        if en_text not in translations:
            print(f"  [{item['f']}] {en_text}")
