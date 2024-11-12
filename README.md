# Claude API Monitor

📊 一个简单但功能强大的 Anthropic Claude API 使用情况监控工具，帮助你实时追踪 API 配额和 Token 使用量。

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ 主要功能

- 🔄 实时监控（每2秒更新）
- 📈 配额和令牌使用量统计
- ⏰ 配额预警提醒
- 🌐 本地时区显示

## 🚀 快速开始

```bash
# 1. 克隆并安装
git clone https://github.com/yourusername/claude-api-monitor.git
cd claude-api-monitor
pip install -r requirements.txt

# 2. 运行监控
./monitor_api_usage.sh -k YOUR_API_KEY

## 📖 使用说明

### 启动方式

1. **命令行参数**
```bash
# 最简单方式（推荐）
./monitor_api_usage.sh -k YOUR_API_KEY

# 或使用 Python 脚本
python anthropic_api_usage_monitor.py -k YOUR_API_KEY

# 使用配置文件
./monitor_api_usage.sh -f /path/to/key.txt

# 使用环境变量
export ANTHROPIC_API_KEY=your_api_key
python anthropic_api_usage_monitor.py
```

### 输出示例
```
==========================================
        Anthropic API 使用情况
==========================================
📊 检查时间: 2024-11-12 17:30:00

🔄 请求配额: 100/5,000 次/分钟 (2.0%)
💭 令牌配额: 1,000/100,000 个/分钟 (1.0%)
⏰ 重置时间: 2024-11-12 17:31:00 CST
```

## 📝 注意事项
- API Key 请妥善保管
- 建议定期监控使用情况

## 📜 许可证
MIT License