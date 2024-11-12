import requests
from datetime import datetime
import pytz
import json
import os

def format_number(num):
    """格式化数字显示"""
    return f"{num:,}"

def calculate_percentage(used, total):
    """计算使用百分比"""
    return (used/total*100 if total else 0)

def analyze_rate_limit_headers(headers):
    """解析并解读速率限制响应头"""
    analysis = []
    
    # 请求限制分析
    req_limit = int(headers.get('anthropic-ratelimit-requests-limit', 0))
    req_remaining = int(headers.get('anthropic-ratelimit-requests-remaining', 0))
    req_used = req_limit - req_remaining
    req_reset = headers.get('anthropic-ratelimit-requests-reset', '')
    
    analysis.append("📊 请求限制分析：")
    analysis.append(f"• 每分钟最多可发送 {req_limit} 个请求")
    analysis.append(f"• 目前已使用 {req_used} 个请求，还剩 {req_remaining} 个可用")
    if req_used > 0:
        analysis.append(f"• 当前请求使用率: {(req_used/req_limit*100):.1f}%")
    
    # 令牌限制分析
    token_limit = int(headers.get('anthropic-ratelimit-tokens-limit', 0))
    token_remaining = int(headers.get('anthropic-ratelimit-tokens-remaining', 0))
    token_used = token_limit - token_remaining
    token_reset = headers.get('anthropic-ratelimit-tokens-reset', '')
    
    analysis.append("\n📝 令牌限制分析：")
    analysis.append(f"• 每分钟最多可使用 {format_number(token_limit)} 个令牌")
    analysis.append(f"• 目前已使用 {format_number(token_used)} 个令牌，还剩 {format_number(token_remaining)} 个可用")
    if token_used > 0:
        analysis.append(f"• 当前令牌使用率: {(token_used/token_limit*100):.1f}%")
    
    # 重置时间分析
    def format_reset_time(reset_time):
        if not reset_time:
            return "未知"
        try:
            utc_time = datetime.strptime(reset_time, '%Y-%m-%dT%H:%M:%SZ')
            utc_time = utc_time.replace(tzinfo=pytz.UTC)
            local_time = utc_time.astimezone()
            now = datetime.now(local_time.tzinfo)
            time_diff = utc_time - now
            minutes = int(time_diff.total_seconds() / 60)
            seconds = int(time_diff.total_seconds() % 60)
            return f"{local_time.strftime('%H:%M:%S')} (还有 {minutes}分{seconds}秒)"
        except Exception:
            return "时间格式解析错误"
    
    analysis.append("\n⏰ 重置时间分析：")
    analysis.append(f"• 请求配额将在 {format_reset_time(req_reset)} 后重置")
    analysis.append(f"• 令牌配额将在 {format_reset_time(token_reset)} 后重置")
    
    # 使用建议
    analysis.append("\n💡 使用建议：")
    if req_remaining < req_limit * 0.2:
        analysis.append("• ⚠️ 请求配额即将耗尽，建议控制请求频率")
    else:
        analysis.append("• ✅ 请求配额充足，可以正常使用")
        
    if token_remaining < token_limit * 0.2:
        analysis.append("• ⚠️ 令牌配额即将耗尽，建议减少大量文本生成")
    else:
        analysis.append("• ✅ 令牌配额充足，可以正常使用")
        
    return "\n".join(analysis)

def check_anthropic_usage(api_key: str):
    """检查 Anthropic API 使用情况并输出详细总结"""
    try:
        # 发送 API 请求
        headers = {
            'x-api-key': api_key,
            'anthropic-version': '2023-06-01',
            'content-type': 'application/json'
        }
        data = {
            "model": "claude-3-sonnet-20240229",
            "max_tokens": 1,
            "messages": [{"role": "user", "content": "hi"}]
        }
        
        response = requests.post(
            'https://api.anthropic.com/v1/messages?beta=true',
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            headers = response.headers
            
            # 转换时间为本地时间
            def utc_to_local(utc_str):
                if not utc_str:
                    return "N/A"
                utc_time = datetime.strptime(utc_str, '%Y-%m-%dT%H:%M:%SZ')
                utc_time = utc_time.replace(tzinfo=pytz.UTC)
                local_time = utc_time.astimezone()
                return local_time.strftime('%Y-%m-%d %H:%M:%S %Z')

            # 获取速率限制信息
            req_remaining = int(headers.get('anthropic-ratelimit-requests-remaining', 0))
            req_limit = int(headers.get('anthropic-ratelimit-requests-limit', 0))
            token_remaining = int(headers.get('anthropic-ratelimit-tokens-remaining', 0))
            token_limit = int(headers.get('anthropic-ratelimit-tokens-limit', 0))
            
            # 计算使用情况
            req_used = req_limit - req_remaining
            token_used = token_limit - token_remaining
            
            # 获取重试时间
            retry_after = headers.get('retry-after', 'N/A')

            print("\n" + "="*50)
            print("           Anthropic API 使用情况详细报告")
            print("="*50)
            
            print(f"\n📊 检查时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            print("\n🔄 【请求配额 (Requests)】")
            print(f"{'总限制:':<15} {format_number(req_limit)} 次/分钟")
            print(f"{'已使用:':<15} {format_number(req_used)} 次")
            print(f"{'使用率:':<15} {calculate_percentage(req_used, req_limit):.1f}%")
            print(f"{'剩余:':<15} {format_number(req_remaining)} 次")
            print(f"{'重置时间:':<15} {utc_to_local(headers.get('anthropic-ratelimit-requests-reset'))}")
            
            print("\n💭 【令牌配额 (Tokens)】")
            print(f"{'总限制:':<15} {format_number(token_limit)} 个/分钟")
            print(f"{'已使用:':<15} {format_number(token_used)} 个")
            print(f"{'使用率:':<15} {calculate_percentage(token_used, token_limit):.1f}%")
            print(f"{'剩余:':<15} {format_number(token_remaining)} 个")
            print(f"{'重置时间:':<15} {utc_to_local(headers.get('anthropic-ratelimit-tokens-reset'))}")
            
            print("\n🔧 【服务器信息】")
            print(f"{'请求ID:':<15} {headers.get('request-id', 'N/A')}")
            print(f"{'服务器:':<15} {headers.get('Server', 'N/A')}")
            print(f"{'连接状态:':<15} {headers.get('Connection', 'N/A')}")
            
            print("\n⚠️ 【限制信息】")
            print(f"{'重试等待时间:':<15} {retry_after} 秒" if retry_after != 'N/A' else f"{'重试等待时间:':<15} 无需等待")
            
            print("\n📋 【原始响应头】")
            rate_limit_headers = {k: v for k, v in headers.items() if 'ratelimit' in k.lower()}
            print(json.dumps(rate_limit_headers, indent=2, ensure_ascii=False))
            
            print("\n📝 【响应头解读】")
            print(analyze_rate_limit_headers(headers))
            
        else:
            print(f"\n❌ 请求失败 (状态码: {response.status_code})")
            print(f"错误信息: {response.text}")
            
    except Exception as e:
        print(f"\n❌ 发生错误: {str(e)}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='监控 Anthropic API 使用情况')
    parser.add_argument('-k', '--key', help='Anthropic API key', required=False)
    parser.add_argument('-f', '--keyfile', help='包含 API key 的文件路径', required=False)
    parser.add_argument('--no-clear', action='store_true', help='不清除屏幕（用于日志记录）')
    
    args = parser.parse_args()
    
    # 获取 API key
    api_key = None
    
    # 从文件读取
    if args.keyfile:
        try:
            with open(args.keyfile, 'r') as f:
                api_key = f.read().strip()
        except Exception as e:
            print(f"读取密钥文件失败: {e}")
            exit(1)
    # 从命令行参数读取
    elif args.key:
        api_key = args.key
    # 从环境变量读取
    elif 'ANTHROPIC_API_KEY' in os.environ:
        api_key = os.environ['ANTHROPIC_API_KEY']
    # 交互式输入
    else:
        api_key = input("请输入你的 Anthropic API key: ").strip()
    
    if not args.no_clear:
        # 清除屏幕
        os.system('clear' if os.name == 'posix' else 'cls')
    
    check_anthropic_usage(api_key)
