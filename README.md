# Ambxst Shell 中文汉化包 🇨🇳

[Ambxst](https://github.com/Axenide/Ambxst) 是一款基于 Quickshell 的高度可定制的 Wayland Shell。本项目提供其中文汉化。

## 安装

```bash
# 1. 克隆本项目
git clone https://github.com/lin-1259/ambxst-zh_CN.git
cd ambxst-zh_CN

# 2. 运行汉化安装脚本
python3 install_zh_CN.py
```

## 效果

- 面板（Bar）界面文字 → 中文
- 控制中心（Dashboard）→ 中文
- 启动器（Launcher）→ 中文
- 通知系统（Notifications）→ 中文
- 锁屏（Lockscreen）→ 中文
- 侧边栏（Sidebar）→ 中文
- 服务状态提示 → 中文
- 其他 UI 文字 → 中文

## 文件结构

```
ambxst-zh_CN/
├── zh_CN.json          # 翻译映射文件（英文 → 中文）
├── install_zh_CN.py    # 安装脚本（自动 patch QML 文件）
├── README.md           # 本文件
└── strings_flat.json   # 扁平格式翻译表（方便协作翻译）
```

## 贡献翻译

编辑 `zh_CN.json`，将空字符串 `""` 替换为对应中文即可。

## 卸载

重新安装 Ambxst 即可恢复英文：

```bash
curl -L get.axeni.de/ambxst | sh
```

## 许可

AGPL-3.0