# Claude API Monitor

📊 一个简单但功能强大的 Anthropic Claude API 使用情况监控工具。实时追踪 API 配额、Token 使用量，帮助你更好地管理 API 资源。

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)

## ✨ 特色功能

- 🔄 **实时监控**: 自动每2秒更新使用情况
- 📈 **详细统计**: 请求配额和令牌使用量的完整统计
- ⏰ **智能提醒**: 配额即将耗尽时主动预警
- 🌐 **本地化时间**: 自动转换为本地时区显示
- 🛠️ **多种使用方式**: 支持命令行、文件、环境变量等多种配置方式
- 🎨 **美观输出**: 格式化的控制台输出，清晰直观

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/claude-api-monitor.git
cd claude-api-monitor

# 安装依赖
pip install -r requirements.txt
```

### 基本使用

1. **快速监控** (推荐)
```bash
./monitor_api_usage.sh -k YOUR_API_KEY
```

2. **单次检查**
```bash
python anthropic_api_usage_monitor.py -k YOUR_API_KEY
```

## 📖 详细使用说明

### 配置方式

1. **命令行参数**
```bash
# 直接使用 API Key
python anthropic_api_usage_monitor.py -k YOUR_API_KEY

# 使用配置文件
python anthropic_api_usage_monitor.py -f /path/to/key.txt

# 不清除屏幕（用于日志记录）
python anthropic_api_usage_monitor.py -k YOUR_API_KEY --no-clear
```

2. **环境变量**
```bash
export ANTHROPIC_API_KEY=your_api_key
python anthropic_api_usage_monitor.py
```

3. **自动监控**
```bash
# 使用 API Key
./monitor_api_usage.sh -k YOUR_API_KEY

# 使用配置文件
./monitor_api_usage.sh -f /path/to/key.txt
```

### 输出说明

监控工具会显示以下信息：
- 📊 **请求配额**
  - 总限制和已使用数量
  - 使用百分比
  - 剩余可用量
- 💭 **令牌配额**
  - Token 总量和已使用量
  - 使用率统计
  - 剩余可用量
- ⏰ **时间信息**
  - 当前检查时间
  - 配额重置时间（本地时区）
- 💡 **使用建议**
  - 根据使用情况提供的建议
  - 接近限制时的预警提示

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！以下是一些贡献方式：
- 报告 bug
- 提出新功能建议
- 改进文档
- 提交代码改进

## 📝 注意事项

- API Key 请妥善保管，不要提交到公共仓库
- 建议定期监控使用情况，避免超出限制
- 如果使用日志记录功能，注意及时清理日志文件

## 📜 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

感谢所有贡献者的支持！

## 📧 联系方式

如有问题或建议，欢迎：
- 提交 [Issue](https://github.com/yourusername/claude-api-monitor/issues)
- 给我发邮件：[your@email.com]
python anthropic_api_usage_monitor.py

# 通过命令行参数提供 API key
python anthropic_api_usage_monitor.py -k YOUR_API_KEY

# 从文件读取 API key
python anthropic_api_usage_monitor.py -f path/to/key_file

# 从环境变量读取（需要先设置 ANTHROPIC_API_KEY 环境变量）
export ANTHROPIC_API_KEY=your_api_key
python anthropic_api_usage_monitor.py
```

使用监控脚本（每2秒自动更新）：
```bash
# 使用 API key
./monitor_api_usage.sh -k YOUR_API_KEY

# 使用包含 API key 的文件
./monitor_api_usage.sh -f path/to/key_file
```

### 命令行参数

Python 脚本支持以下参数：
- `-k, --key`: 直接指定 Anthropic API key
- `-f, --keyfile`: 指定包含 API key 的文件路径
- `--no-clear`: 不清除屏幕（用于日志记录）

监控脚本支持以下参数：
- `-k`: 直接指定 API key
- `-f`: 指定包含 API key 的文件路径

### 输出示例

```
==================================================
           Anthropic API 使用情况详细报告
==================================================

📊 检查时间: 2024-11-12 17:30:00

🔄 【请求配额 (Requests)】
总限制:         5,000 次/分钟
已使用:         100 次
使用率:         2.0%
剩余:           4,900 次
重置时间:       2024-11-12 17:31:00 CST

💭 【令牌配额 (Tokens)】
总限制:         100,000 个/分钟
已使用:         1,000 个
使用率:         1.0%
剩余:           99,000 个
重置时间:       2024-11-12 17:31:00 CST
```

### 功能特点

- 支持本地时间显示
- 美观的格式化数字显示
- 详细的使用报告
- 完整的错误处理
- 用户友好的界面

### 注意事项

- 请确保妥善保管你的 API key
- 建议定期监控使用情况
- 当使用率接近限制时，考虑实施请求节流

### 贡献

欢迎提交 Issues 和 Pull Requests！

### 许可证

MIT License