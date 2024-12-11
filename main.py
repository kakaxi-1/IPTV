from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 验证 token_360 是否正确加载
print(f"token_360: {os.getenv('token_360')}")
import json
import os
import re
import time
import asyncio
from datetime import datetime, timedelta
import threading
import requests
import aiohttp
from github import Github
import subprocess
import sys



# 安装依赖，如果尚未安装
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "flask"])

# 导入你的模块
import requests
from flask import Flask

with open('data/config.json', 'r', encoding='utf-8') as json_file:
    config = json.load(json_file)
ISP_LIST = config['ISP_LIST'] # 运营商列表
CITY_LIST = config['CITY_LIST'] # 城市列表
MIN_DOWNLOAD_SPEED = config['MIN_DOWNLOAD_SPEED'] # 最小下载速度

def should_run():
    """判断是否需要运行程序"""
    if not os.path.exists("data/config.json"):
        return True

    with open("data/config.json", 'r', encoding='utf-8') as json_file:
        config = json.load(json_file)
        last_run_time_str = config.get('last_run_time', '')
        last_run_time = datetime.strptime(last_run_time_str, '%Y-%m-%d %H:%M:%S') if last_run_time_str else datetime.min
        current_time = datetime.now()

    return (current_time - last_run_time) >= timedelta(days=1)

def update_run_time():
    """更新上次运行时间"""
    with open("data/config.json", 'r+', encoding='utf-8') as json_file:
        config = json.load(json_file)
        config['last_run_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        json_file.seek(0)
        json.dump(config, json_file, ensure_ascii=False, indent=4)
        json_file.truncate()

def read_file(file_path):
    """读取文件内容"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

def read_json_file(file_path):
    """读取 JSON 文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"文件 {file_path} 读取错误：{e}")
        return {}

def write_json_file(file_path, data):
    """将数据写入 JSON 文件"""
    merged_data = merge_and_deduplicate(data, read_json_file(file_path))
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(merged_data, file, ensure_ascii=False, indent=4)
        print(f"数据已成功写入文件：{file_path}")
    except Exception as e:
        print(f"写入 JSON 文件时出错：{e}")

def remove_duplicate_ips(json_data):
    """对每个省份的 IP 地址列表去重"""
    for key, value in json_data.items():
        json_data[key] = list(set(value))
    return json_data

def merge_and_deduplicate(json1, json2):
    """合并两个相同格式的 JSON 数据，并对列表中的值去重"""
    merged_json = {}
    for key in set(json1.keys()).union(set(json2.keys())):
        list1 = json1.get(key, [])
        list2 = json2.get(key, [])
        merged_json[key] = list(set(list1 + list2))
    return merged_json

def get_ip(token, size=10):
    """根据城市和运营商信息，从 API 获取对应 IP 和端口"""

    result_data = {}
    headers = {
        "X-QuakeToken": token,
        "Content-Type": "application/json"
    }

    for city in CITY_LIST:
        for isp in ISP_LIST:
            print(f"正在查询城市 {city}, 运营商 {isp} 的 IP 地址...")
            query = f'((country: "china" AND app:"udpxy") AND province_cn: "{city}") AND isp: "中国{isp}"'
            data = {
                "query": query,
                "start": 0,
                "size": size,
                "ignore_cache": False,
                "latest": True,
                "shortcuts": ["610ce2adb1a2e3e1632e67b1"]
            }

            try:
                response = requests.post(
                    url="https://quake.360.net/api/v3/search/quake_service",
                    headers=headers,
                    json=data,
                    timeout=10
                )

                if response.status_code == 200:
                    ip_data = response.json().get("data", [])
                    urls = [f"http://{entry.get('ip')}:{entry.get('port')}" for entry in ip_data]
                    if urls:
                        result_data[f"{city}{isp}"] = urls
                        print(f"成功获取 {city}, {isp} 的 IP 地址！")
                        print(f"可用 IP 地址：{urls}")
                else:
                    print(f"城市 {city}, 运营商 {isp} 查询失败，状态码：{response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"查询城市 {city}, 运营商 {isp} 时出错：{e}")
            time.sleep(3)       

    return result_data

async def test_and_get_ip_info(province_ips):
    """测试 UDPxy 代理是否可用，仅返回可用 IP 的省份信息"""
    print("测试 UDPxy 代理（异步）")

    async def check_ip(province, ip):
        try:
            test_url = f"{ip}/status/"
            async with aiohttp.ClientSession() as session:
                async with session.get(test_url, timeout=3) as response:
                    if response.status == 200:
                        page_content = await response.text()
                        if 'udpxy' in page_content:
                            return province, ip
        except:
            pass
        return None, None

    tasks = [check_ip(province, ip) for province, ip_list in province_ips.items() for ip in ip_list]
    available_ips = await asyncio.gather(*tasks)

    working_ips = {}
    for province, ip in filter(lambda x: x[0] is not None, available_ips):
        if province not in working_ips:
            working_ips[province] = []
        working_ips[province].append(ip)

    return remove_duplicate_ips(working_ips)

def process_ip_list(ip_list):
    """拼接组播 URL 并返回数据"""
    output_data = {}

    def process_channels(ip_url, channels, speed=0):
        combined_results = []
        for name, multicast_url in channels:
            combined_info = f"{name},{ip_url}{multicast_url},{speed}"
            combined_results.append(combined_info)
        return combined_results

    for province, ip_urls in ip_list.items():
        multicast_file_path = os.path.join("udp", f"{province}.txt")
        if os.path.exists(multicast_file_path):
            with open(multicast_file_path, 'r', encoding='utf-8') as multicast_file:
                channels = [(line.strip().split(',')[0], line.strip().split(',')[1]) for line in multicast_file if len(line.strip().split(',')) == 2]
                for ip_url in ip_urls:
                    output_data[ip_url] = process_channels(ip_url, channels)

    return output_data

def natural_key(string_):
    """将字符串转换为自然排序的 key"""
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', string_)]

def group_and_sort_channels(channel_data):
    """根据规则分组并排序频道信息"""
    groups = {
        '央视频道': [],
        '卫视频道': [],
        '其他频道': [],
        '未分组': []
    }

    for channel_info in channel_data:
        if isinstance(channel_info, list):
            channel_info = ','.join(map(str, channel_info))

        if isinstance(channel_info, str):
            parts = channel_info.split(',')
            if len(parts) == 3:
                name, url, speed = parts[0], parts[1], float(parts[2])
            else:
                print(f"无效数据格式：{channel_info}，跳过该频道")
                continue

            if speed < 0.1:
                continue

            if 'cctv' in name.lower():
                groups['央视频道'].append((name, url, speed))
            elif '卫视' in name or '凤凰' in name:
                groups['卫视频道'].append((name, url, speed))
            else:
                groups['其他频道'].append((name, url, speed))

    for group_name, group in groups.items():
        if group_name == '央视频道':
            group.sort(key=lambda x: (natural_key(x[0]), -x[2] if x[2] is not None else float('-inf')))
        else:
            group.sort(key=lambda x: (len(x[0]), natural_key(x[0]), -x[2] if x[2] is not None else float('-inf')))

    with open("itvlist.txt", 'w', encoding='utf-8') as file:
        for group_name, channel_list in groups.items():
            file.write(f"{group_name},#genre#\n")
            for name, url, speed in channel_list:
                file.write(f"{name},{url},{speed}\n")
            file.write("\n")

        new_time = datetime.now() + timedelta(hours=8)
        new_time_str = new_time.strftime("%m-%d %H:%M")

        file.write(f"{new_time_str},#genre#:\n{new_time_str},https://raw.gitmirror.com/MemoryCollection/IPTV/main/TB/mv.mp4\n")

    print("分组后的频道信息已保存到 itvlist.txt ")
    return groups

def download_speed_test(ip_list):
    """测试下载速度并返回可用 IP 列表"""

    def download_file(url):
        try:
            start_time = time.time()
            response = requests.get(url, stream=True, timeout=3)
            total_data = 0
            for chunk in response.iter_content(1024):
                total_data += len(chunk)
                if time.time() - start_time >= 3:
                    break
            return total_data / 3 / (1024 * 1024)
        except Exception:
            return 0

    def test_single_ip(ip, channels):
        speeds = []
        for channel in channels[:4]:
            _, url, _ = channel.split(",")
            speed = download_file(url)
            speeds.append(speed)
        return speeds

    def process_ip(ip, channels):
        speeds = test_single_ip(ip, channels)
        if speeds.count(0) > 2:
            avg_speed = 0
        else:
            avg_speed = sum(speeds) / len(speeds) if speeds else 0
        updated_channels = [
            f"{name},{url},{avg_speed:.2f}" for channel in channels
            for name, url, _ in [channel.split(",")]
        ]
        return updated_channels

    results = {}
    lock = threading.Lock()
    progress = [0]

    def worker(ip, channels):
        updated_channels = process_ip(ip, channels)
        with lock:
            results[ip] = updated_channels
            progress[0] += 1
            print(f"Progress: {progress[0]} / {len(ip_list)}")

    threads = []
    for ip, channels in ip_list.items():
        while len(threads) >= 6:
            threads = [t for t in threads if t.is_alive()]
            time.sleep(0.1)
        thread = threading.Thread(target=worker, args=(ip, channels))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    filtered_channels = []
    for ip, channels in results.items():
        for channel in channels:
            name, url, speed = channel.split(",")
            if float(speed) >= MIN_DOWNLOAD_SPEED:
                filtered_channels.append(channel)

    os.makedirs("data", exist_ok=True)
    with open("data/itv.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(filtered_channels))

    return filtered_channels

def upload_file_to_github(token, repo_name, file_path, folder='', branch='main'):
    """将结果上传到 GitHub"""
    g = Github(token)
    repo = g.get_user().get_repo(repo_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    git_path = f"{folder}/{file_path.split('/')[-1]}" if folder else file_path.split('/')[-1]

    try:
        contents = repo.get_contents(git_path, ref=branch)
    except:
        contents = None

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        if contents:
            repo.update_file(contents.path, current_time, content, contents.sha, branch=branch)
            print("文件已更新")
        else:
            repo.create_file(git_path, current_time, content, branch=branch)
            print("文件已创建")
    except Exception as e:
        print("文件上传失败:", e)

def main():

    token_360 = os.getenv("token_360")

    if not token_360:
        print("未设置：token_360，程序无法执行")
        return True

    if should_run():
        update_run_time()
        ip_list = get_ip(token_360)
        ip_list = merge_and_deduplicate(ip_list, read_json_file("data/iplist.json"))
    else:
        ip_list = read_json_file("data/iplist.json")
    ip_list = asyncio.run(test_and_get_ip_info(ip_list))
    write_json_file("data/iplist.json", ip_list)
    ip_list = process_ip_list(ip_list)
    ip_list = download_speed_test(ip_list)
    group_and_sort_channels(ip_list)

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    if GITHUB_TOKEN:
        upload_file_to_github(GITHUB_TOKEN, "IPTV", "itvlist.txt")

if __name__ == "__main__":
    main()
