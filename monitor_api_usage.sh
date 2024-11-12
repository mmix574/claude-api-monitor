#!/bin/bash

# 检查命令行参数
if [ $# -eq 0 ]; then
    echo "使用方法: $0 [-k API_KEY | -f KEY_FILE]"
    echo "选项:"
    echo "  -k API_KEY   直接指定 API key"
    echo "  -f KEY_FILE  指定包含 API key 的文件路径"
    exit 1
fi

# 解析命令行参数
while getopts "k:f:" opt; do
    case $opt in
        k)
            KEY_ARG="-k $OPTARG"
            ;;
        f)
            KEY_ARG="-f $OPTARG"
            ;;
        \?)
            echo "无效的选项: -$OPTARG" >&2
            exit 1
            ;;
        :)
            echo "选项 -$OPTARG 需要参数." >&2
            exit 1
            ;;
    esac
done

# 检查是否存在 Python 脚本
if [ ! -f "anthropic_api_usage_monitor.py" ]; then
    echo "错误: 找不到 anthropic_api_usage_monitor.py 文件"
    exit 1
fi

# 定义信号处理函数
cleanup() {
    echo -e "\n正在退出监控..."
    tput cnorm  # 恢复光标
    exit 0
}

# 设置信号处理
trap cleanup SIGINT SIGTERM

# 隐藏光标
tput civis

echo "开始监控 Anthropic API 使用情况..."
echo "按 Ctrl+C 退出"
echo

# 无限循环执行监控
while true; do
    # 执行 Python 脚本并传入参数
    # --no-clear 参数确保输出保持在同一位置
    python3 anthropic_api_usage_monitor.py $KEY_ARG --no-clear
    
    # 等待 2 秒
    sleep 2
    
    # 移动光标到顶部
    tput cup 0 0
done