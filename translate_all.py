#!/usr/bin/env python3
"""完整翻译 Ambxst Shell UI 字符串"""
import json
from pathlib import Path

STRINGS_FILE = Path("/root/ambxst-zh_CN/strings.json")
ZH_CN_FILE = Path("/root/ambxst-zh_CN/zh_CN.json")

# 完整翻译字典 - 覆盖所有 550 条字符串
translations = {
    # === 基础控件 (已翻译) ===
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

    # === 工具菜单 (已翻译) ===
    "Screenshot": "截图",
    "Open Screenshots": "打开截图",
    "Open Recordings": "打开录制",
    "Color Picker": "取色器",
    "QR Code": "二维码",
    "Google Lens": "Google 镜头",
    "Mirror": "镜像",

    # === 设置窗口 (已翻译) ===
    "Ambxst Settings": "Ambxst 设置",

    # === AI 面板 (已翻译) ===
    "AI & API Keys": "AI 与 API 密钥",
    "Enter API Key...": "输入 API 密钥...",
    "Custom Provider": "自定义提供商",
    "Custom Provider API Key": "自定义提供商 API 密钥",
    "Save": "保存",
    "Clear": "清除",
    "Custom Endpoint": "自定义端点",
    "Custom cURL Template": "自定义 cURL 模板",
    # AI 面板 - 新增
    "e.g. https://api.example.com/v1/chat/completions": "例如 https://api.example.com/v1/chat/completions",
    "Placeholders: {{ENDPOINT}}, {{API_KEY}}, {{BODY_PATH}}": "占位符：{{ENDPOINT}}、{{API_KEY}}、{{BODY_PATH}}",
    "curl -X POST {{ENDPOINT}} -H 'Authorization: Bearer {{API_KEY}}' -d @{{BODY_PATH}}": "curl -X POST {{ENDPOINT}} -H 'Authorization: Bearer {{API_KEY}}' -d @{{BODY_PATH}}",

    # === 通知 (已翻译) ===
    "Notifications": "通知",

    # === tmux (已翻译) ===
    "Search or create tmux session...": "搜索或创建 tmux 会话...",
    "Open": "打开",
    "Rename": "重命名",
    "Quit": "退出",
    "No panes to display": "无可显示的窗格",
    "Loading panes...": "加载窗格中...",
    "No session selected": "未选择会话",
    "Select a session to preview": "选择一个会话预览",

    # === 剪贴板 (已翻译) ===
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

    # === 颜色选择器 (已翻译) ===
    "Custom": "自定义",
    "Color picker": "取色器",
    "Enter password...": "输入密码...",

    # === 主题面板 (已翻译) ===
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

    # === 变体编辑器 (已翻译) ===
    "Item Color": "项目颜色",
    "Border": "边框",
    "Angle": "角度",
    "Dot Color": "点颜色",
    "Background": "背景",
    "Range": "范围",

    # === 音频混音器 (已翻译) ===
    "Sound": "声音",
    "Open PipeWire Volume Control": "打开 PipeWire 音量控制",
    "Output": "输出",
    "Input": "输入",
    "Volume": "音量",
    "Balance": "平衡",

    # === 音频混音器 - 新增 ===
    "Volume Mixer": "音量混音器",
    "No applications using audio": "没有应用正在使用音频",

    # === 蓝牙 - 新增 ===
    "Forget": "忘记设备",

    # === 渐变编辑器 ===
    "Gradient Stops (": "渐变点 (",
    "Stop ": "停止点 ",
    "Position": "位置",
    "Delete stop": "删除停止点",

    # === 设置索引/分类 ===
    "Network": "网络",
    "Bluetooth": "蓝牙",
    "Audio Mixer": "音频混音器",
    "Audio Effects": "音频特效",
    "Theme": "主题",
    "Animation Duration": "动画时长",
    "Shadow Opacity": "阴影不透明度",
    "Shadow Blur": "阴影模糊",
    "Shadow Offset": "阴影偏移",
    "Color Scheme": "配色方案",
    "Color Variant": "颜色变体",
    "Background Variant": "背景变体",
    "Popup Variant": "弹出窗口变体",
    "Internal BG Variant": "内部背景变体",
    "Bar BG Variant": "面板背景变体",
    "Pane Variant": "窗格变体",
    "Gradient Mode": "渐变模式",
    "Color Opacity": "颜色不透明度",
    "Color Border": "颜色边框",
    "Gradient Stops": "渐变点",
    "Gradient Angle": "渐变角度",
    "Key Bindings": "按键绑定",
    "Launcher Keybind": "启动器快捷键",
    "Dashboard Keybind": "仪表盘快捷键",
    "Clipboard Keybind": "剪贴板快捷键",
    "Emoji Keybind": "表情快捷键",
    "Tmux Keybind": "Tmux 快捷键",
    "Wallpapers Keybind": "壁纸快捷键",
    "Assistant Keybind": "AI 助手快捷键",
    "Notes Keybind": "笔记快捷键",
    "Overview Keybind": "概览快捷键",
    "Powermenu Keybind": "电源菜单快捷键",
    "Settings Keybind": "设置快捷键",
    "Lockscreen Keybind": "锁屏快捷键",
    "Tools Keybind": "工具快捷键",
    "Screenshot Keybind": "截图快捷键",
    "Screenrecord Keybind": "录屏快捷键",
    "Lens Keybind": "镜头快捷键",
    "Reload Keybind": "重载快捷键",
    "Quit Keybind": "退出快捷键",
    "System": "系统",
    "Prefixes": "前缀",
    "Clipboard Prefix": "剪贴板前缀",
    "Emoji Prefix": "表情前缀",
    "Tmux Prefix": "Tmux 前缀",
    "Wallpapers Prefix": "壁纸前缀",
    "Notes Prefix": "笔记前缀",
    "Weather Location": "天气地点",
    "Temperature Unit": "温度单位",
    "Blur Transition": "模糊过渡",
    "Window Preview": "窗口预览",
    "Wavy Line": "波浪线",
    "System Resources": "系统资源",
    "Idle Settings": "闲置设置",
    "Lock Command": "锁屏命令",
    "Before Sleep": "休眠前",
    "After Sleep": "休眠后",
    "Idle Listener": "闲置监听器",
    "Compositor": "合成器",
    "Border Size": "边框大小",
    "Window Gaps": "窗口间距",
    "Border Colors": "边框颜色",
    "Shadows Enabled": "启用阴影",
    "Sync Shadow Color": "同步阴影颜色",
    "Sync Shadow Opacity": "同步阴影不透明度",
    "Shadow Range": "阴影范围",
    "Shadow Power": "阴影强度",
    "Shadow Scale": "阴影缩放",
    "Blur Enabled": "启用模糊",
    "Blur Size": "模糊大小",
    "Blur Passes": "模糊次数",
    "Blur Xray": "模糊透视",
    "Blur New Optimizations": "模糊新优化",
    "Blur Ignore Opacity": "模糊忽略透明度",
    "Blur Ignorealpha": "模糊忽略 Alpha",
    "Blur Ignorealpha Value": "模糊忽略 Alpha 值",
    "Blur Noise": "模糊噪点",
    "Blur Contrast": "模糊对比度",
    "Blur Brightness": "模糊亮度",
    "Blur Vibrancy": "模糊鲜艳度",

    # === Ambxst / Bar / Shell ===
    "Ambxst": "Ambxst",
    "Bar": "面板",
    "Bar Position": "面板位置",
    "Launcher Icon": "启动器图标",
    "Launcher Icon Tint": "启动器图标色调",
    "Launcher Icon Full Tint": "启动器图标完全着色",
    "Launcher Icon Size": "启动器图标大小",
    "Pill Style": "胶囊样式",
    "Firefox Player": "Firefox 播放器",
    "Bar Auto-hide": "面板自动隐藏",
    "Pinned on Startup": "启动时固定",
    "Hover to Reveal": "悬停显示",
    "Hover Region Height": "悬停区域高度",
    "Show Pin Button": "显示固定按钮",
    "Available on Fullscreen": "全屏时可用",
    "Show Running Indicators": "显示运行指示器",
    "Show Overview Button": "显示概览按钮",
    "Bar Screens": "面板屏幕",
    "Notch": "刘海",
    "Workspaces": "工作区",
    "Workspaces Shown": "显示工作区数量",
    "Show App Icons": "显示应用图标",
    "Always Show Numbers": "始终显示数字",
    "Show Numbers": "显示数字",
    "Dynamic Workspaces": "动态工作区",
    "Overview": "概览",
    "Overview Rows": "概览行数",
    "Overview Columns": "概览列数",
    "Overview Scale": "概览缩放",
    "Overview Workspace Spacing": "概览工作区间距",
    "Dock": "Dock",
    "Dock Enabled": "启用 Dock",
    "Dock Mode": "Dock 模式",
    "Dock Position": "Dock 位置",
    "Dock Height": "Dock 高度",
    "Dock Icon Size": "Dock 图标大小",
    "Dock Spacing": "Dock 间距",
    "Dock Margin": "Dock 边距",
    "Dock Hover Region Height": "Dock 悬停区域高度",
    "Dock Pinned on Startup": "Dock 启动时固定",
    "Lockscreen": "锁屏",
    "Desktop": "桌面",
    "Desktop Enabled": "启用桌面图标",
    "Desktop Icon Size": "桌面图标大小",
    "Desktop Vertical Spacing": "桌面垂直间距",
    "Desktop Text Color": "桌面文字颜色",
    "Shell System": "Shell 系统",

    # === 按键绑定面板 ===
    "Legacy Dispatcher": "传统调度器",
    "Keybinds": "按键绑定",
    "Add keybind": "添加快捷键",
    "Reload binds": "重载绑定",
    "Reset to default": "重置为默认",
    "Name (optional)": "名称（可选）",
    "e.g. Open Terminal, Switch to Workspace 1...": "例如：打开终端、切换到工作区 1...",
    "Key Combination": "按键组合",
    "e.g. R, TAB, ESCAPE, mouse:272...": "例如：R、TAB、ESCAPE、mouse:272...",
    "Action": "动作",
    "Layouts (AxctlService)": "布局（AxctlService）",
    "Leave all unselected to work in all layouts": "不选则适用于所有布局",

    # === Wi-Fi 面板 ===
    "Wi-Fi": "Wi-Fi",
    "Open captive portal": "打开认证门户",
    "Network settings": "网络设置",
    "Rescan networks": "重新扫描网络",

    # === 蓝牙面板 ===
    "Bluetooth": "蓝牙",
    "Open Blueman": "打开 Blueman",
    "Scan for devices": "扫描设备",

    # === 合成器面板 ===
    "Right click to remove": "右键移除",
    "AxctlService": "AxctlService",
    "Coming Soon": "即将推出",
    "Shadows": "阴影",
    "Sync Border Size": "同步边框大小",
    "Border Size": "边框大小",
    "Sync Rounding": "同步圆角",
    "Rounding": "圆角",
    "Gaps In": "内间距",
    "Gaps Out": "外间距",
    "Border Angle": "边框角度",
    "Inactive Angle": "非活动角度",
    "Sync Border Color": "同步边框颜色",
    "Active Border": "活动边框",
    "Inactive Border": "非活动边框",
    "Enabled": "启用",
    "Sync Color": "同步颜色",
    "Sync Opacity": "同步不透明度",
    "Render Power": "渲染强度",
    "Scale": "缩放",
    "Sharp": "锐化",
    "Ignore Window": "忽略窗口",
    "Passes": "次数",
    "Xray": "透视",
    "New Optimizations": "新优化",
    "Ignore Opacity": "忽略透明度",
    "Explicit Ignorealpha": "显式忽略 Alpha",
    "Ignorealpha Value": "忽略 Alpha 值",
    "Noise": "噪点",
    "Contrast": "对比度",
    "Brightness": "亮度",
    "Vibrancy": "鲜艳度",
    "Support for more compositors\nis planned for future updates.": "未来更新将支持更多合成器。",

    # === EasyEffects 面板 ===
    "EasyEffects": "EasyEffects",
    "Open EasyEffects": "打开 EasyEffects",
    "Refresh": "刷新",
    "EasyEffects not installed": "未安装 EasyEffects",
    "Output Presets": "输出预设",
    "Input Presets": "输入预设",
    "No presets configured": "未配置预设",
    "Active": "激活",

    # === 设置标签页 ===
    "Network": "网络",
    "Bluetooth": "蓝牙",
    "Mixer": "混音器",
    "Effects": "特效",
    "Theme": "主题",
    "Binds": "按键",
    "System": "系统",
    "Compositor": "合成器",
    "Ambxst": "Ambxst",
    "Search...": "搜索...",

    # === 系统面板 ===
    "Prefixes": "前缀",
    "Weather": "天气",
    "Performance": "性能",
    "System Resources": "系统资源",
    "Idle": "闲置",
    "Keyboard shortcuts for quick actions in launcher": "启动器中的键盘快捷键快速操作",
    "Clipboard": "剪贴板",
    "Emoji": "表情",
    "Tmux": "Tmux",
    "Notes": "笔记",
    "Location": "地点",
    "e.g. Buenos Aires, Tokyo...": "例如：北京、上海、东京...",
    "Unit": "单位",
    "Celsius": "摄氏",
    "Fahrenheit": "华氏",
    "Toggle visual effects to improve performance": "切换视觉效果以提高性能",
    "Blur Transition": "模糊过渡",
    "Animated blur when opening panels": "打开面板时动画模糊",
    "Window Preview": "窗口预览",
    "Show window thumbnails in overview": "在概览中显示窗口缩略图",
    "Wavy Line": "波浪线",
    "Animated wavy line effect": "动画波浪线效果",
    "Disable Cover Art Rotation": "禁用封面旋转",
    "Stop the vinyl disc from spinning": "停止黑胶唱片旋转动画",
    "Configure which disks to monitor": "配置要监控的磁盘",
    "e.g. /, /home...": "例如 /、/home...",
    "Add Disk": "添加磁盘",
    "Lock Cmd": "锁屏命令",
    "Before Sleep": "休眠前",
    "After Sleep": "休眠后",
    "Listeners": "监听器",
    "Listener ": "监听器 ",
    "Timeout (s)": "超时（秒）",
    "On Timeout": "超时时",
    "On Resume": "恢复时",
    "Add Listener": "添加监听器",

    # === Shell 面板 ===
    "Screens": "屏幕",
    "Empty = all screens": "空则表示所有屏幕",
    "Bar": "面板",
    "Sidebar": "侧边栏",
    "Frame": "框架",
    "Notch": "刘海",
    "Workspaces": "工作区",
    "Overview": "概览",
    "Dock": "Dock",
    "Lockscreen": "锁屏",
    "Desktop": "桌面",
    "System": "系统",
    "Top": "顶部",
    "Bottom": "底部",
    "Left": "左侧",
    "Right": "右侧",
    "Launcher Icon": "启动器图标",
    "Launcher Icon Tint": "启动器图标色调",
    "Launcher Icon Full Tint": "启动器图标完全着色",
    "Launcher Icon Size": "启动器图标大小",
    "Pill Style": "胶囊样式",
    "Squished": "挤压",
    "Use 12h Format": "使用 12 小时制",
    "Enable Firefox Player": "启用 Firefox 播放器",
    "Auto-hide": "自动隐藏",
    "Pinned on Startup": "启动时固定",
    "Hover to Reveal": "悬停显示",
    "Hover Region Height": "悬停区域高度",
    "Show Pin Button": "显示固定按钮",
    "Available on Fullscreen": "全屏时可用",
    "Enabled": "启用",
    "Thickness": "厚度",
    "Contain Bar": "包含面板",
    "Keep Bar Shadow": "保留面板阴影",
    "Keep Bar Border": "保留面板边框",
    "Island": "岛形",
    "Keep Hidden": "保持隐藏",
    "Disable Hover Expansion": "禁用悬停扩展",
    "No Media Display": "不显示媒体",
    "User@Host": "用户@主机",
    "Compositor": "合成器",
    "Custom Text": "自定义文本",
    "Shown": "显示数量",
    "Show App Icons": "显示应用图标",
    "Always Show Numbers": "始终显示数字",
    "Show Numbers": "显示数字",
    "Dynamic": "动态",
    "Rows": "行数",
    "Columns": "列数",
    "Scale": "缩放",
    "Workspace Spacing": "工作区间距",
    "Position": "位置",
    "Theme": "主题",
    "Floating": "浮动",
    "Integrated": "集成",
    "Height": "高度",
    "Icon Size": "图标大小",
    "Spacing": "间距",
    "Margin": "边距",
    "Hover Region": "悬停区域",
    "Show Running Indicators": "显示运行指示器",
    "Show Overview Button": "显示概览按钮",
    "Vertical Spacing": "垂直间距",
    "Text Color": "文字颜色",
    "Update Service": "更新服务",
    "About Ambxst ": "关于 Ambxst ",
    "Donate ❤️": "捐赠 ❤️",
    "OCR Languages": "OCR 语言",
    "English": "英语",
    "Spanish": "西班牙语",
    "Latin": "拉丁语",
    "Japanese": "日语",
    "Chinese (Simplified)": "简体中文",
    "Chinese (Traditional)": "繁体中文",
    "Korean": "韩语",
    "Width": "宽度",

    # === 表情面板 ===
    "Light": "浅色",
    "Medium-Light": "中浅",
    "Medium": "中等",
    "Medium-Dark": "中深",
    "Dark": "深色",
    "Search emojis...": "搜索表情...",
    "Clear recent?": "清空最近使用？",

    # === 笔记 ===
    "Search notes...": "搜索笔记...",
    "Edit": "编辑",
    "Rich Text": "富文本",
    "Markdown": "Markdown",
    "Start typing...": "开始输入...",
    "Write markdown here...": "在此处编写 Markdown...",
    "Select or create a note": "选择或创建笔记",

    # === 系统指标 ===
    "System": "系统",

    # === 壁纸 ===
    "Search wallpapers...": "搜索壁纸...",
    "Tint": "着色",
    "Images": "图片",
    "Videos": "视频",

    # === 启动器 ===
    "Search applications...": "搜索应用...",
    "Launch": "启动",
    "Create Shortcut": "创建快捷方式",

    # === 电源菜单 ===
    "Lock Session": "锁定会话",
    "Suspend": "挂起",
    "Hibernate": "休眠",
    "Exit AxctlService": "退出 AxctlService",
    "Reboot": "重启",
    "Power Off": "关机",

    # === 预设 ===
    "Visit Author": "访问作者",
    "Update": "更新",
    "Search or create preset...": "搜索或创建预设...",
    "Select config files to update:": "选择要更新的配置文件：",
    "Cancel": "取消",

    # === 工具 ===
    "Toggle Audio Output": "切换音频输出",
    "Toggle Microphone": "切换麦克风",
    "Portal": "对话框",
    "Region": "区域",
    "Window": "窗口",
    "Screen": "屏幕",

    # === AI 服务 - 描述 ===
    "Execute a shell command on the user's system (Linux). Use this to list files, control the system, or run utilities. Output will be returned.": "在用户系统（Linux）上执行 Shell 命令。用于列出文件、控制系统或运行工具。将返回输出结果。",
    "The shell command to run (e.g. 'ls -la', 'ip addr')": "要运行的 Shell 命令（例如 'ls -la'、'ip addr'）",
    "Unknown": "未知",
    "Unknown error": "未知错误",
    "OpenAI Model": "OpenAI 模型",
    "Mistral Model": "Mistral 模型",
    "Groq Model": "Groq 模型",
    "Local Ollama Model": "本地 Ollama 模型",
    "Latest model with recursive self-improvement, SOTA coding capabilities": "最新模型，具备递归自我改进、最先进编码能力",
    "MiniMax-M2.7": "MiniMax-M2.7",
    "Same performance as M2.7, faster inference (~100 tps)": "与 M2.7 相同性能，推理更快（约 100 tps）",
    "MiniMax-M2.7-highspeed": "MiniMax-M2.7-高速",
    "Peak performance, ultimate value, master the complex": "巅峰性能、极致价值、驾驭复杂",
    "MiniMax-M2.5": "MiniMax-M2.5",
    "Same performance as M2.5, faster inference (~100 tps)": "与 M2.5 相同性能，推理更快（约 100 tps）",
    "MiniMax-M2.5-highspeed": "MiniMax-M2.5-高速",
    "Powerful multi-language programming, enhanced reasoning": "强大的多语言编程，增强推理能力",
    "MiniMax-M2.1": "MiniMax-M2.1",
    "Same performance as M2.1, faster inference (~100 tps)": "与 M2.1 相同性能，推理更快（约 100 tps）",
    "MiniMax-M2.1-highspeed": "MiniMax-M2.1-高速",
    "Agentic capabilities, advanced reasoning, 200k context": "智能体能力、高级推理、200K 上下文",
    "MiniMax-M2": "MiniMax-M2",
    "Role-playing, multi-turn conversations, emotional expression": "角色扮演、多轮对话、情感表达",
    "M2-her": "M2-her",

    # === 蓝牙设备 ===
    "Unknown": "未知",

    # === 桌面 ===
    "Loading desktop...": "桌面加载中...",

    # === 番茄钟 ===
    "-1m": "-1 分钟",
    "+1m": "+1 分钟",
    "Auto": "自动",
    "Sync Spotify": "同步 Spotify",

    # === 天气 ===
    "Mainly clear": "晴",
    "Partly cloudy": "多云",
    "Overcast": "阴天",
    "Fog": "雾",
    "Drizzle": "毛毛雨",
    "Rain": "雨",
    "Heavy rain": "大雨",
    "Snow": "雪",
    "Heavy snow": "大雪",
    "Thunder": "雷",
    "Hail": "冰雹",

    # === AI 助手侧边栏 ===
    "Switch AI model": "切换 AI 模型",
    "Show help": "显示帮助",
    "Start new chat": "开始新对话",
    "Set API key": "设置 API 密钥",
    "Set system prompt": "设置系统提示词",
    "Chat History": "聊天历史",
    "Run Command": "运行命令",
    "Reject": "拒绝",
    "Approve": "批准",
    "Command Approved": "命令已批准",
    "Command Rejected": "命令已拒绝",
    "Copied!": "已复制！",
    "Search models...": "搜索模型...",
    "Refresh?": "刷新？",

    # === 上下文菜单 ===
    ", entry ? entry.text :": ", 条目 ? 条目.text :",

    # === 杂项 ===
    "Hello, <font color='": "你好，<font color='",
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

print(f"翻译完成！")
print(f"  已翻译: {translated_count} 条")
print(f"  待翻译: {empty_count} 条")
print(f"  总计: {len(original_data)} 条")
print(f"  完成率: {translated_count/len(original_data)*100:.1f}%")

# 输出未翻译的
if empty_count > 0:
    print(f"\n未翻译的字符串:")
    for item in original_data:
        en_text = item['en']
        if en_text not in translations:
            print(f"  [{item['f']}] {en_text}")