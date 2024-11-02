import os
import requests
import re
import cv2
import datetime
from datetime import datetime


files = os.listdir('rtp')
files_name = []

for file in files:
    name, extension = os.path.splitext(file)
    files_name.append(name)


provinces_isps = [name for name in files_name if name.count('_') == 1]
print(f"本次查询：{provinces_isps}的组播节目")

keywords = []


for province_isp in provinces_isps:
    try:
        with open(f'rtp/{province_isp}.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines if line.strip()]

        if lines:
            first_line = lines[0]
            if "rtp://" in first_line:
                mcast = first_line.split("rtp://")[1].split(" ")[0]
                keywords.append(province_isp + "_" + mcast)
    except FileNotFoundError:
        print(f"文件 '{province_isp}.txt' 不存在. 跳过此文件.")


for keyword in keywords:
    province, isp, mcast = keyword.split("_")


    search_url = f"http://tonkiang.us/hoteliptv.php?X-UCXHRREQUESTID=173056148226441189"
    current_time = datetime.now()
    
    try:
  
        print(f"{current_time} 查询运营商 : {province}{isp} ，查询网址 : {search_url}")
        response = requests.get(search_url, timeout=5)
        response.raise_for_status()

     
        pattern = r"http://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+"
        urls_all = re.findall(pattern, response.text)
        result_urls = set(urls_all)

        print(f"{current_time} 查询到的UDP源: {result_urls}")

        valid_ips = []

      
        for url in result_urls:
            video_url = url + "/rtp/" + mcast
            cap = cv2.VideoCapture(video_url)

            if not cap.isOpened():
                print(f"{current_time} {video_url} 无效")
            else:
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                print(f"{current_time} {video_url} 的分辨率为 {width}x{height}")

                if width > 0 and height > 0:
                    valid_ips.append(url)

                cap.release()

  
        if valid_ips:
            rtp_filename = f'rtp/{province}_{isp}.txt'
            with open(rtp_filename, 'r', encoding='utf-8') as file:
                data = file.read()
            txt_filename = f'txt_files/{province}{isp}.txt'
            with open(txt_filename, 'w') as new_file:
                for url in valid_ips:
                    new_data = data.replace("rtp://", f"{url}/rtp/")
                    new_file.write(new_data)

            print(f'已生成播放列表，保存至 {txt_filename}')

    except requests.RequestException as e:
        print(f"{current_time} 查询发生异常: {e}")

print('节目表制作完成！ 文件输出在 txt_files 目录下！')