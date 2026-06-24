# Ambxst Shell 中文汉化包 🇨🇳

将 Ambxst Shell 界面完整翻译为简体中文。

## 快速使用

```bash
# 1️⃣ 下载汉化包
git clone https://github.com/lin-1259/ambxst-zh_CN.git
cd ambxst-zh_CN

# 2️⃣ 一键安装汉化
python3 install_zh_CN.py

# 3️⃣ 重启 Ambxst
# 按 Super+Shift+R 重载，或重新登录
```

就是这么简单，不需要任何配置，脚本会自动找到 Ambxst 的安装位置并打补丁。

如果需要恢复英文，运行：

```bash
python3 install_zh_CN.py --undo
```

## 翻译进度

| 项目 | 数值 |
|------|:----:|
| 翻译字符串 | **617 条** |
| 覆盖 QML 文件 | **69 个** |
| 翻译完成度 | **100% ✅** |

## 文件说明

```
ambxst-zh_CN/
├── zh_CN.json          # ✅ 翻译数据（直接用这个安装）
├── install_zh_CN.py     # ✅ 一键安装脚本
├── strings.json         # 原始字符串提取（仅供开发参考）
└── translate_all.py     # 翻译字典脚本（仅供开发参考）
```

## 兼容性

- 适用于 Ambx Shell 最新版本
- 支持 Hyprland 环境
- 安装前会自动备份原文件