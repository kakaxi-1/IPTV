import requests
import re
import os

# 设定要抓取的URL
search_url = 'http://tonkiang.us/hoteliptv.php?X-UCXHRREQUESTID=173056538411615534'
# 设定要替换的目标文件路径
target_file_path = 'txt_files/北京电信.txt'

def fetch_ip_ports(url):
    """ 从指定URL抓取IP:端口信息 """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 检查请求是否成功
        # 使用正则表达式匹配IP:端口
        pattern = r"http://(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)"
        ip_ports = re.findall(pattern, response.text)
        return ip_ports
    except requests.RequestException as e:
        print(f"抓取数据时发生错误: {e}")
        return []

def replace_ip_ports_in_file(ip_ports, file_path):
    """ 替换指定文件中的IP:端口信息 """
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 替换内容
        for ip_port in ip_ports:
            # 替换内容，替换 http:// 和 /rtp/ 之间的部分
            content = re.sub(r"http://.*?/rtp/", f"http://{ip_port}/rtp/", content, count=1)

        # 保存替换后的内容到文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"已将新的IP:端口信息写入到 {file_path}")
    else:
        print(f"文件 '{file_path}' 不存在.")

# 主程序
ip_ports = fetch_ip_ports(search_url)
if ip_ports:
    print(f"抓取到的IP:端口信息: {ip_ports}")
    replace_ip_ports_in_file(ip_ports, target_file_path)
else:
    print("未抓取到有效的IP:端口信息。")