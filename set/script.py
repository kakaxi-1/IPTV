import cv2 

import time

from datetime import datetime, timedelta

from collections import defaultdict

import concurrent.futures

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import requests

import re

import os

import threading

from queue import Queue

from datetime import datetime

import replace

import fileinput


# merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1##
## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## merge-1## 
#enter
exclude_strings = ['121.207.104', 'xeace.cn:8888', '//27.10', '//220.176.218', '//171.221.129', '//118.122.111', '//27.191.71', '//175.11.171', '//220.176.218', '//117.43.80', '//182.139.152', '//118.122.111', '//118.112.60', '//27.191.71', '//122.232.188', '//125.71.44', '//122.234.77', '//122.232.188', '//14.105.105.35', '//27.191.71.248', '//144.255.40.160', '//140.250.221', '//223.242.146', '//182.139.215', '//182.150.168', '//120.32.11', '//113.86.204.209', '//110.185.44', '///61.157.92.168', '//59.56.214', '//117.25.38', '//125.82.171', '//117.12.148', '//183.5.92', '//117.66.231', '//36.47.83', '//115.221.95', '//113.120.108', '//115.193.167', '//117.28.112', '//117.25.38', '//117.67.169', '//221.15.251', '//117.67.169', '//221.15.251', '//116.5.168', '//175.0.95', '//118.248.154', '//220.175.144', '//118.254.201', '//14.154.192', '//124.112.208', '//182.148.30', '//110.185.70', '//183.5.97.206', '//123.55.112', '//222.182.115', '//14.117.233', '//113.13.242', '//59.56.214.134', '//58.42.184.132', '//58.42.184.132', '//220.192.1.40', '//27.11.253.19', '//27.11.58.239', '//14.105.104', '//183.54.208.185', '//116.252.77.132', '//221.232.175', '//144.255.44.24', '//113.222.42.190', '//61.150.11', '//110.185.10', '//118.254', '//122.232.188', '//171.116.157', '//125.43.40', '//125.86.181', '//27.153.80', '//61.190.129.1', '//182.46.8', '//119.130.11', '//58.63.65', '//1.84.218', '//183.184', '//171.217.81', '//27.190.83.', '//1.197.1', '//58.46.249', '//125.71.170', '//119.4.15', '//222.138.213', '//222.138.213', '//222.94.90', '//222.95.95', '//117.69', '//60.168.228', '//223.215.43', '//223.240.250', '//60.171.98', '//27.151.150', '//+', '//+', '//+', '//+', '//+']
#enter
file_paths = ["txt_files/北京联通.txt", "txt_files/江西电信.txt", "txt_files/河北电信.txt", "txt_files/湖北电信.txt", "txt_files/河南联通.txt", "txt_files/Sus.txt"]

#enter
with open("txt_files/Kmerga2H+OLD.txt", "w", encoding="utf-8") as output:
    #enter
    for file_path in file_paths:
        #enter
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                #enter
                if not any(exclude_string in line for exclude_string in exclude_strings):
                    #enter
                    output.write(line)


	
# SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1
## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1## SPDTST-1

#enter
tested_ips = {}

#enter
lines = []
with open('txt_files/Kmerga2H+OLD.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

#enter
for line in lines:
    #enter
    if line.count(',') == 1:
        #enter
        ip_start = line.find(',') + 1
        rtp_pos = line.find('rtp')
        if rtp_pos != -1:
            ip_part = line[ip_start:rtp_pos].strip()
        else:
            #enter
            ip_part = line[ip_start:].strip()

        url_start = ip_start
        url_end = line.find('$')
        if url_end != -1:
            url = line[url_start:url_end].strip()
        else:
            #enter
            url = line[url_start:].strip()

        #enter
        if ip_part in tested_ips:
            print(f"enterIP: {ip_part}")
            continue

        #enter
        cap = cv2.VideoCapture(url)

        #enter
        start_time = time.time()
        frame_count = 0

        #enter
        while frame_count < 9999 and (time.time() - start_time) < 10:  # enter
            ret, frame = cap.read()
            if not ret:  # enter
                break  # enter
            frame_count += 1  #enter

        #enter
        if frame_count >200:  #enter
            tested_ips[ip_part] = {'status': 'ok', 'frame_count': frame_count}
        else:
            tested_ips[ip_part] = {'status': 'tested', 'frame_count': frame_count}

        #enter
        cap.release()

#enter
with open('txt_files/Kmerga2H+OLD-SPD.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        #enter,enter
        if line.count(',') == 1:
            #enter
            ip_start = line.find(',') + 1
            rtp_pos = line.find('rtp')
            if rtp_pos != -1:
                channel_ip = line[ip_start:rtp_pos].strip()

                #enter
                if channel_ip in tested_ips and tested_ips[channel_ip]['status'] == 'ok':
                    #enter
                    file.write(f"{line.strip()}\n")
                    #enter
                    frame_count = tested_ips[channel_ip]['frame_count']
                    file.write(f">SPD{frame_count}\n")
	

# merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2##
## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## merge-2## 
#enter
exclude_strings = ['121.207.104', 'xeace.cn:8888', '//27.10', '//220.176.218', '//171.221.129', '//118.122.111', '//27.191.71', '//175.11.171', '//220.176.218', '//117.43.80', '//182.139.152', '//118.122.111', '//118.112.60', '//27.191.71', '//122.232.188', '//125.71.44', '//122.234.77', '//122.232.188', '//14.105.105.35', '//27.191.71.248', '//144.255.40.160', '//140.250.221', '//223.242.146', '//182.139.215', '//182.150.168', '//120.32.11', '//113.86.204.209', '//110.185.44', '///61.157.92.168', '//59.56.214', '//117.25.38', '//125.82.171', '//117.12.148', '//183.5.92', '//117.66.231', '//36.47.83', '//115.221.95', '//113.120.108', '//115.193.167', '//117.28.112', '//117.25.38', '//117.67.169', '//221.15.251', '//117.67.169', '//221.15.251', '//116.5.168', '//175.0.95', '//118.248.154', '//220.175.144', '//118.254.201', '//14.154.192', '//124.112.208', '//182.148.30', '//110.185.70', '//183.5.97.206', '//123.55.112', '//222.182.115', '//14.117.233', '//113.13.242', '//59.56.214.134', '//58.42.184.132', '//58.42.184.132', '//220.192.1.40', '//27.11.253.19', '//27.11.58.239', '//14.105.104', '//183.54.208.185', '//116.252.77.132', '//221.232.175', '//144.255.44.24', '//113.222.42.190', '//61.150.11', '//110.185.10', '//118.254', '//122.232.188', '//171.116.157', '//125.43.40', '//125.86.181', '//27.153.80', '//61.190.129.1', '//182.46.8', '//119.130.11', '//58.63.65', '//1.84.218', '//183.184', '//171.217.81', '//27.190.83.', '//1.197.1', '//58.46.249', '//125.71.170', '//119.4.15', '//222.138.213', '//222.138.213', '//222.94.90', '//222.95.95', '//117.69', '//60.168.228', '//223.215.43', '//223.240.250', '//60.171.98', '//27.151.150', '//+', '//+', '//+', '//+', '//+']

#enter
file_paths = ["txt_files/江苏电信.txt", "txt_files/天津联通.txt", "txt_files/河南电信.txt", "txt_files/广西电信.txt", "txt_files/Susa.txt"]

#enter
with open("txt_files/Kmergalow2H+lowOLD.txt", "w", encoding="utf-8") as output:
    #enter
    for file_path in file_paths:
        #enter
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                #enter
                if not any(exclude_string in line for exclude_string in exclude_strings):
                    #enter
                    output.write(line)


# SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2
## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2## SPDTST-2

#enter
tested_ips = {}

#enter
lines = []
with open('txt_files/Kmergalow2H+lowOLD.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

#enter
for line in lines:
    #enter
    if line.count(',') == 1:
        #enter
        ip_start = line.find(',') + 1
        rtp_pos = line.find('rtp')
        if rtp_pos != -1:
            ip_part = line[ip_start:rtp_pos].strip()
        else:
            #enter
            ip_part = line[ip_start:].strip()

        url_start = ip_start
        url_end = line.find('$')
        if url_end != -1:
            url = line[url_start:url_end].strip()
        else:
            #enter
            url = line[url_start:].strip()

        #enter
        if ip_part in tested_ips:
            print(f"enterIP: {ip_part}")
            continue

        #enter
        cap = cv2.VideoCapture(url)

        #enter
        start_time = time.time()
        frame_count = 0

        #enter
        while frame_count < 9999 and (time.time() - start_time) < 10:  # enter
            ret, frame = cap.read()
            if not ret:  # enter
                break  # enter
            frame_count += 1  #enter

        #enter
        if frame_count >150:  #enter
            tested_ips[ip_part] = {'status': 'ok', 'frame_count': frame_count}
        else:
            tested_ips[ip_part] = {'status': 'tested', 'frame_count': frame_count}

        #enter
        cap.release()

#enter
with open('txt_files/Kmergalow2H+lowOLD-SPD.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        #enter,enter
        if line.count(',') == 1:
            #enter
            ip_start = line.find(',') + 1
            rtp_pos = line.find('rtp')
            if rtp_pos != -1:
                channel_ip = line[ip_start:rtp_pos].strip()

                #enter
                if channel_ip in tested_ips and tested_ips[channel_ip]['status'] == 'ok':
                    #enter
                    file.write(f"{line.strip()}\n")
                    #enter
                    frame_count = tested_ips[channel_ip]['frame_count']
                    file.write(f">SPD{frame_count}\n")




# merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3##
## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## merge-3## 
#enter
exclude_strings = ['121.207.104', 'xeace.cn:8888', '//27.10', '//220.176.218', '//171.221.129', '//118.122.111', '//27.191.71', '//175.11.171', '//220.176.218', '//117.43.80', '//182.139.152', '//118.122.111', '//118.112.60', '//27.191.71', '//122.232.188', '//125.71.44', '//122.234.77', '//122.232.188', '//14.105.105.35', '//27.191.71.248', '//144.255.40.160', '//140.250.221', '//223.242.146', '//182.139.215', '//182.150.168', '//120.32.11', '//113.86.204.209', '//110.185.44', '///61.157.92.168', '//59.56.214', '//117.25.38', '//125.82.171', '//117.12.148', '//183.5.92', '//117.66.231', '//36.47.83', '//115.221.95', '//113.120.108', '//115.193.167', '//117.28.112', '//117.25.38', '//117.67.169', '//221.15.251', '//117.67.169', '//221.15.251', '//116.5.168', '//175.0.95', '//118.248.154', '//220.175.144', '//118.254.201', '//14.154.192', '//124.112.208', '//182.148.30', '//110.185.70', '//183.5.97.206', '//123.55.112', '//222.182.115', '//14.117.233', '//113.13.242', '//59.56.214.134', '//58.42.184.132', '//58.42.184.132', '//220.192.1.40', '//27.11.253.19', '//27.11.58.239', '//14.105.104', '//183.54.208.185', '//116.252.77.132', '//221.232.175', '//144.255.44.24', '//113.222.42.190', '//61.150.11', '//110.185.10', '//118.254', '//122.232.188', '//171.116.157', '//125.43.40', '//125.86.181', '//27.153.80', '//61.190.129.1', '//182.46.8', '//119.130.11', '//58.63.65', '//1.84.218', '//183.184', '//171.217.81', '//27.190.83.', '//1.197.1', '//58.46.249', '//125.71.170', '//119.4.15', '//222.138.213', '//222.138.213', '//222.94.90', '//222.95.95', '//117.69', '//60.168.228', '//223.215.43', '//223.240.250', '//60.171.98', '//27.151.150', '//+', '//+', '//+', '//+', '//+']

#enter
file_paths = ["txt_files/四川电信.txt", "txt_files/重庆电信.txt", "txt_files/湖南电信.txt", "txt_files/浙江电信.txt", "txt_files/Susaw.txt"]

#enter
with open("txt_files/Kmergaverylow2H+verylowOLD.txt", "w", encoding="utf-8") as output:
    #enter
    for file_path in file_paths:
        #enter
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                #enter
                if not any(exclude_string in line for exclude_string in exclude_strings):
                    #enter
                    output.write(line)


# SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3
## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3## SPDTST-3

#enter
tested_ips = {}

#enter
lines = []
with open('txt_files/Kmergaverylow2H+verylowOLD.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

#enter
for line in lines:
    #enter
    if line.count(',') == 1:
        #enter
        ip_start = line.find(',') + 1
        rtp_pos = line.find('rtp')
        if rtp_pos != -1:
            ip_part = line[ip_start:rtp_pos].strip()
        else:
            #enter
            ip_part = line[ip_start:].strip()

        url_start = ip_start
        url_end = line.find('$')
        if url_end != -1:
            url = line[url_start:url_end].strip()
        else:
            #enter
            url = line[url_start:].strip()

        #enter
        if ip_part in tested_ips:
            print(f"enterIP: {ip_part}")
            continue

        #enter
        cap = cv2.VideoCapture(url)

        #enter
        start_time = time.time()
        frame_count = 0

        #enter
        while frame_count < 9999 and (time.time() - start_time) < 10:  # enter
            ret, frame = cap.read()
            if not ret:  # enter
                break  # enter
            frame_count += 1  #enter

        #enter
        if frame_count >10:  #enter
            tested_ips[ip_part] = {'status': 'ok', 'frame_count': frame_count}
        else:
            tested_ips[ip_part] = {'status': 'tested', 'frame_count': frame_count}

        #enter
        cap.release()

#enter
with open('txt_files/Kmergaverylow2H+verylowOLD-SPD.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        #enter,enter
        if line.count(',') == 1:
            #enter
            ip_start = line.find(',') + 1
            rtp_pos = line.find('rtp')
            if rtp_pos != -1:
                channel_ip = line[ip_start:rtp_pos].strip()

                #enter
                if channel_ip in tested_ips and tested_ips[channel_ip]['status'] == 'ok':
                    #enter
                    file.write(f"{line.strip()}\n")
                    #enter
                    frame_count = tested_ips[channel_ip]['frame_count']
                    file.write(f">SPD{frame_count}\n")






# SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4
## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4## SPDTST-4

#enter
tested_ips = {}

#enter
lines = []
with open('txt_files/gaa.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

#enter
for line in lines:
    #enter
    if line.count(',') == 1:
        #enter
        ip_start = line.find(',') + 1
        rtp_pos = line.find('rtp')
        if rtp_pos != -1:
            ip_part = line[ip_start:rtp_pos].strip()
        else:
            #enter
            ip_part = line[ip_start:].strip()

        url_start = ip_start
        url_end = line.find('$')
        if url_end != -1:
            url = line[url_start:url_end].strip()
        else:
            #enter
            url = line[url_start:].strip()

        #enter
        if ip_part in tested_ips:
            print(f"enterIP: {ip_part}")
            continue

        #enter
        cap = cv2.VideoCapture(url)

        #enter
        start_time = time.time()
        frame_count = 0

        #enter
        while frame_count < 9999 and (time.time() - start_time) < 10:  # enter
            ret, frame = cap.read()
            if not ret:  # enter
                break  # enter
            frame_count += 1  #enter

        #enter
        if frame_count >190:  #enter
            tested_ips[ip_part] = {'status': 'ok', 'frame_count': frame_count}
        else:
            tested_ips[ip_part] = {'status': 'tested', 'frame_count': frame_count}

        #enter
        cap.release()

#enter
with open('txt_files/gaa-SPD.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        #enter,enter
        if line.count(',') == 1:
            #enter
            ip_start = line.find(',') + 1
            rtp_pos = line.find('rtp')
            if rtp_pos != -1:
                channel_ip = line[ip_start:rtp_pos].strip()

                #enter
                if channel_ip in tested_ips and tested_ips[channel_ip]['status'] == 'ok':
                    #enter
                    file.write(f"{line.strip()}\n")
                    #enter
                    frame_count = tested_ips[channel_ip]['frame_count']
                    file.write(f">SPD{frame_count}\n")





# SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5
## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5## SPDTST-5

#enter
tested_ips = {}

#enter
lines = []
with open('txt_files/gaar.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

#enter
for line in lines:
    #enter
    if line.count(',') == 1:
        #enter
        ip_start = line.find(',') + 1
        rtp_pos = line.find('rtp')
        if rtp_pos != -1:
            ip_part = line[ip_start:rtp_pos].strip()
        else:
            #enter
            ip_part = line[ip_start:].strip()

        url_start = ip_start
        url_end = line.find('$')
        if url_end != -1:
            url = line[url_start:url_end].strip()
        else:
            #enter
            url = line[url_start:].strip()

        #enter
        if ip_part in tested_ips:
            print(f"enterIP: {ip_part}")
            continue

        #enter
        cap = cv2.VideoCapture(url)

        #enter
        start_time = time.time()
        frame_count = 0

        #enter
        while frame_count < 9999 and (time.time() - start_time) < 10:  # enter
            ret, frame = cap.read()
            if not ret:  # enter
                break  # enter
            frame_count += 1  #enter

        #enter
        if frame_count >80:  #enter
            tested_ips[ip_part] = {'status': 'ok', 'frame_count': frame_count}
        else:
            tested_ips[ip_part] = {'status': 'tested', 'frame_count': frame_count}

        #enter
        cap.release()

#enter
with open('txt_files/gaar-SPD.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        #enter,enter
        if line.count(',') == 1:
            #enter
            ip_start = line.find(',') + 1
            rtp_pos = line.find('rtp')
            if rtp_pos != -1:
                channel_ip = line[ip_start:rtp_pos].strip()

                #enter
                if channel_ip in tested_ips and tested_ips[channel_ip]['status'] == 'ok':
                    #enter
                    file.write(f"{line.strip()}\n")
                    #enter
                    frame_count = tested_ips[channel_ip]['frame_count']
                    file.write(f">SPD{frame_count}\n")



#enter###################
#enter###################
#enter###################
#enter###################
#enter###################
#enter###################
#enter###################
#enter###################




#enter
with open('txt_files/Kmerga2H+OLD-SPD.txt', 'r', encoding='utf-8') as file_in:
    #enter
    with open('txt_files/Kmerga2H+OLD-SPDjump.txt', 'w', encoding='utf-8') as file_out:
        #enter
        for line in file_in:
            #enter
            file_out.write(line)

# enter
#enter
seen_lines = set()

#enter
with open('txt_files/Kmerga2H+OLD-SPDjump.txt', 'r', encoding='utf-8') as file_in, \
     open('txt_files/Sus.txt', 'w', encoding='utf-8') as file_out:
    #enter文件
    for line in file_in:
        #enter
        stripped_line = line.strip()
        if stripped_line not in seen_lines:
            #enter
            file_out.write(line)
            seen_lines.add(stripped_line)
			
			

#enter
with open('txt_files/Kmergalow2H+lowOLD-SPD.txt', 'r', encoding='utf-8') as file_in:
    #enter
    with open('txt_files/Kmergalow2H+lowOLD-SPDjump.txt', 'w', encoding='utf-8') as file_out:
        #enter
        for line in file_in:
            #enter
            file_out.write(line)

# enter
#enter
seen_lines = set()

#enter
with open('txt_files/Kmergalow2H+lowOLD-SPDjump.txt', 'r', encoding='utf-8') as file_in, \
     open('txt_files/Susa.txt', 'w', encoding='utf-8') as file_out:
    #enter文件
    for line in file_in:
        #enter
        stripped_line = line.strip()
        if stripped_line not in seen_lines:
            #enter
            file_out.write(line)
            seen_lines.add(stripped_line)


#enter
with open('txt_files/Kmergaverylow2H+verylowOLD-SPD.txt', 'r', encoding='utf-8') as file_in:
    #enter
    with open('txt_files/Kmergaverylow2H+verylowOLD-SPDjump.txt', 'w', encoding='utf-8') as file_out:
        #enter
        for line in file_in:
            #enter
            file_out.write(line)

# enter
#enter
seen_lines = set()

#enter
with open('txt_files/Kmergaverylow2H+verylowOLD-SPDjump.txt', 'r', encoding='utf-8') as file_in, \
     open('txt_files/Susaw.txt', 'w', encoding='utf-8') as file_out:
    #enter文件
    for line in file_in:
        #enter
        stripped_line = line.strip()
        if stripped_line not in seen_lines:
            #enter
            file_out.write(line)
            seen_lines.add(stripped_line)



#IP_SAVEenter

#enter
current_time = datetime.now()
#enter
future_time = current_time + timedelta(hours=8)
#enter
formatted_future_time = future_time.strftime("%Y-%m-%d %H:%M:%S")

#enter
with open('txt_files/IP_address.txt', 'a', encoding='utf-8') as file:
    file.write('\n' * 2)  # enter
    file.write(formatted_future_time + '\n')  # enter
    file.write('\n')  # enter

print("enter ok。")

#1############################################################################split##


#enter
#enter
keywords = ['S川A爱科幻','天JD都市高清','安HH生活时尚','山DB农科','山XD都市剧场','广DA经济科教','广XH南宁都市','江S南京生活','江XB都市剧场','河BA农民高清','河N民生频道','河NC电视剧频道','浙JC教育高清','湖N常德新闻','福JA少儿','辽LD沈阳新闻','重QD影视频道','陕XA新闻资讯']  
pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('txt_files/Kmerga2H+OLD.txt', 'r', encoding='utf-8') as file, open('txt_files/IP_address.txt', 'a', encoding='utf-8') as IP_address:

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         IP_address.write(line)  #go
		 
		 
#enter
#enter		 
keywords = ['S川A爱科幻','天JD都市高清','安HH生活时尚','山DB农科','山XD都市剧场','广DA经济科教','广XH南宁都市','江S南京生活','江XB都市剧场','河BA农民高清','河N民生频道','河NC电视剧频道','浙JC教育高清','湖N常德新闻','福JA少儿','辽LD沈阳新闻','重QD影视频道','陕XA新闻资讯']  
pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter	 
with open('txt_files/Kmergalow2H+lowOLD.txt', 'r', encoding='utf-8') as file, open('txt_files/IP_address.txt', 'a', encoding='utf-8') as IP_address:

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         IP_address.write(line)  #enter 
		 
		 
		 
		 
#enter
#enter		 
keywords = ['S川A爱科幻','天JD都市高清','安HH生活时尚','山DB农科','山XD都市剧场','广DA经济科教','广XH南宁都市','江S南京生活','江XB都市剧场','河BA农民高清','河N民生频道','河NC电视剧频道','浙JC教育高清','湖N常德新闻','福JA少儿','辽LD沈阳新闻','重QD影视频道','陕XA新闻资讯']  
pattern = '|'.join(keywords)  #enterenter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter	 
with open('txt_files/Kmergaverylow2H+verylowOLD.txt', 'r', encoding='utf-8') as file, open('txt_files/IP_address.txt', 'a', encoding='utf-8') as IP_address:

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         IP_address.write(line)  #enter 		 

#########################split##



#enter
with open('txt_files/IP_address.txt', 'r', encoding='utf-8') as file_in:
    # go
    with open('txt_files/IP_addressjump.txt', 'w', encoding='utf-8') as file_out:
        #entertxt_files/IP_address.txt
        for line in file_in:
            #entertxt_files/IP_addressjump.txt
            file_out.write(line)

# enter
#enter
seen_lines = set()

#enter
with open('txt_files/IP_addressjump.txt', 'r', encoding='utf-8') as file_in, \
     open('txt_files/IP_address.txt', 'w', encoding='utf-8') as file_out:
    #enter txt_files/IP_addressjump.txt
    for line in file_in:
        #enter
        stripped_line = line.strip()
        if stripped_line not in seen_lines:
            #enter
            file_out.write(line)
            seen_lines.add(stripped_line)
			
			
			
			
#enter###################
#enter###################
#enter###################
#enter###################
#enter###################
#enter###################
#enter###################
#enter###################





import time

import concurrent.futures

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import requests

import re

import os

import threading

from queue import Queue

from datetime import datetime

import replace

import fileinput




file_contents = []   #enter

#enter
file_paths = ['txt_files/Sus.txt','txt_files/Susa.txt','txt_files/Susaw.txt','txt_files/gaa-SPD.txt','txt_files/gaar-SPD.txt',"txt_files/ga.txt"]



for file_path in file_paths:

    with open(file_path, 'r', encoding="utf-8") as file:

        content = file.read()

        file_contents.append(content)


#enter

with open("txt_files/merga.txt", "w", encoding="utf-8") as output:

    output.write('\n'.join(file_contents))


#替换

for line in fileinput.input("txt_files/merga.txt", inplace=True):  #enter

    line = line.replace("CCTV10", "CCTW10")

    line = line.replace("CCTV11", "CCTW11")

    line = line.replace("CCTV12", "CCTW12")

    line = line.replace("CCTV13", "CCTW13")

    line = line.replace("CCTV14", "CCTW14")

    line = line.replace("CCTV15", "CCTW15")

    line = line.replace("CCTV16", "CCTW16")

    line = line.replace("CCTV17", "CCTW17")

    #enter

    line = line.replace("CCTV1综合", "CCTV1")

    line = line.replace("CCTV2财经", "CCTV2")

    line = line.replace("CCTV3综艺", "CCTV3")

    line = line.replace("CCTV4中文国际", "CCTV4")

    line = line.replace("CCTV4美洲", "CCTV4美")

    line = line.replace("CCTV4欧洲", "CCTV4欧")

    line = line.replace("CCTV5体育", "CCTV5")

    line = line.replace("CCTV5+体育", "CCTV5+")

    line = line.replace("CCTV6电影", "CCTV6")

    line = line.replace("CCTV7军事", "CCTV7")

    line = line.replace("CCTV7军农", "CCTV7")

    line = line.replace("CCTV7农业", "CCTV7")

    line = line.replace("CCTV7国防军事", "CCTV7")

    line = line.replace("CCTV8电视剧", "CCTV8")

    line = line.replace("CCTV9纪录", "CCTV9")

    line = line.replace("CCTV9记录", "CCTV9")

    line = line.replace("CCTV9纪录", "CCTV9")

    line = line.replace("CCTV10科教", "CCTV10")

    line = line.replace("CCTV11戏曲", "CCTV11")

    line = line.replace("CCTV12社会与法", "CCTV12")

    line = line.replace("CCTV13新闻", "CCTV13")

    line = line.replace("CCTV新闻", "CCTV13")

    line = line.replace("CCTV14少儿", "CCTV14")

    line = line.replace("央视14少儿", "CCTV14")

    line = line.replace("CCTV少儿超", "CCTV14")

    line = line.replace("CCTV15音乐", "CCTV15")

    line = line.replace("CCTV音乐", "CCTV15")

    line = line.replace("CCTV16奥林匹克", "CCTV16")

    line = line.replace("CCTV17农业农村", "CCTV17")

    line = line.replace("CCTV17军农", "CCTV17")

    line = line.replace("CCTV17农业", "CCTV17")

    line = line.replace("CCTV5+体育赛视", "CCTV5+")

    line = line.replace("CCTV5+赛视", "CCTV5+")

    line = line.replace("CCTV5+体育赛事", "CCTV5+")

    line = line.replace("CCTV5+赛事", "CCTV5+")

    line = line.replace("CCTV5+体育", "CCTV5+")

    line = line.replace("CCTV5赛事", "CCTV5+")



    print(line, end="")  #enter



#enter####################################################################################################

for line in fileinput.input("txt_files/merga.txt", inplace=True):  #enter

    
    line = line.replace("CCTV10", "CCTW10")

    line = line.replace("CCTV11", "CCTW11")

    line = line.replace("CCTV12", "CCTW12")

    line = line.replace("CCTV13", "CCTW13")

    line = line.replace("CCTV14", "CCTW14")

    line = line.replace("CCTV15", "CCTW15")

    line = line.replace("CCTV16", "CCTW16")

    line = line.replace("CCTV17", "CCTW17")


    print(line, end="")  #enter



#enter####################################################################################################################



with open('txt_files/merga.txt', 'r', encoding='utf-8') as f:

    lines = f.readlines()


lines.sort()


with open('txt_files/排序.txt', 'w', encoding='UTF-8') as f:

    for line in lines:

        f.write(line)


#enter##########################################################################################################################

for line in fileinput.input("txt_files/排序.txt", inplace=True):  #enter

    line = line.replace("CCTW10", "CCTV10")

    line = line.replace("CCTW11", "CCTV11")

    line = line.replace("CCTW12", "CCTV12")

    line = line.replace("CCTW13", "CCTV13")

    line = line.replace("CCTW14", "CCTV14")

    line = line.replace("CCTW15", "CCTV15")

    line = line.replace("CCTW16", "CCTV16")

    line = line.replace("CCTW17", "CCTV17")


    print(line, end="")  #enter

 ##################################################################################################################################SPLIT#
 
 
 
 

# enter
with open('txt_files/g.txt', 'r', encoding='utf-8') as file1:
  
    #enter
    with open('txt_files/TT1.txt', 'w', encoding='utf-8') as file2:
        #enter
        for line in file1:
            #enter
            file2.write(line)


#star#########################
#enter#############################################################################################

keywords = ['CCTV','CCTV欧','CCTV美','CETV', 'CF', 'IPT淘', 'CHC', 'IWA', '凤凰卫视', '星空', 'CHANNEL', 'W','卫视', 'X','Y']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('txt_files/排序.txt', 'r', encoding='utf-8') as file, open('txt_files/T1.txt', 'w', encoding='utf-8') as T1:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T1.write(line)  #enter

for line in fileinput.input("txt_files/T1.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter
with open('txt_files/TT1.txt', 'a', encoding='utf-8') as TT1:    #####enter

    TT1.write('\n#shougong\n')        
 
    print(line, end="")  #enter 
#enter

#enter
import re

#enter
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # enter
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # enter
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  #enter
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('txt_files/T1.txt', 'r', encoding="utf-8") as input_file, open('txt_files/TT1.txt', 'a', encoding="utf-8") as output_file:
    #enter
    lines = input_file.readlines()

    #enter
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    #enter
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################

 ##################################################################################################################################SPLIT#

#star#########################
#enter#############################################################################################



#starmerga多个文件到一个文件###########

file_contents = []

file_paths = ["txt_files/TT1.txt"] 

for file_path in file_paths:

    with open(file_path, 'r', encoding="utf-8") as file:

        content = file.read()

        file_contents.append(content)



# enter

with open("txt_files/AMER-start.txt", "w", encoding="utf-8") as output:

    output.write('\n'.join(file_contents))

#enter
##################################################################################################################################SPLIT#
  
  

#star
with open('txt_files/AMER-start.txt', 'r', encoding='utf-8') as file:
    content = file.read()

#enter
content = content.replace("WA", "").replace("WP", "").replace("WB", "").replace("WC", "").replace("WD", "").replace("WE", "").replace("WF", "").replace("WG", "").replace("WH", "").replace("WI", "").replace("WJ", "").replace("WK", "").replace("WL", "").replace("WM", "").replace("WN", "").replace("WO", "").replace("WP", "").replace("WQ", "").replace("WR", "").replace("WS", "").replace("WT", "").replace("WU", "").replace("WV", "").replace("WW", "").replace("WX", "").replace("WY", "").replace("WZ", "").replace("CF", "").replace("IV", "").replace("X纪实", "纪实").replace("Y动漫", "动漫").replace("Y金色学堂", "金色学堂").replace("电Y", "电影").replace("老DY", "老电影").replace("X乐", "乐").replace("X求", "求").replace("X纪", "纪").replace("X记", "记").replace("Y新", "新").replace("剧J", "连续剧").replace("重Q", "重庆").replace("北J", "北京").replace("河B", "河北").replace("河N", "河南").replace("天J", "天津").replace("湖B", "湖北").replace("湖N", "湖南").replace("山D", "山东").replace("安H", "安徽").replace("江S", "江苏").replace("山X", "山西").replace("浙J", "浙江").replace("辽L", "辽宁").replace("吉L", "吉林").replace("贵Z", "贵州").replace("陕X", "陕西").replace("S川", "四川").replace("褔J", "福建").replace("GAT-", "").replace("裾J", "裾集").replace("江X", "江西").replace("新J", "新疆").replace("褔JA", "福建").replace("褔JB", "福建").replace("褔JC", "福建").replace("褔JD", "福建").replace("福J", "福建").replace("广X", "广西").replace("A", "").replace("B", "").replace("F", "").replace("G", "").replace("I", "").replace("J", "").replace("K", "").replace("L", "").replace("M", "").replace("N", "").replace("O", "").replace("P", "").replace("Q", "").replace("R", "").replace("S", "").replace("U", "").replace("W", "").replace("X", "").replace("Y", "").replace("Z", "").replace("C新闻", "新闻").replace("电映C", "电映").replace("电映E", "电映").replace("电映H", "电映").replace("D影视", "影视").replace("E都市", "都市").replace("H新农", "新农").replace("河北C", "河北").replace("河北D", "河北").replace("河南C", "河南").replace("河南D", "河南").replace("天津C", "天津").replace("天津D", "天津").replace("天津E", "天津").replace("广D", "广东").replace("广东C", "广东").replace("广东H", "广东").replace("广西C", "广西").replace("广西D", "广西").replace("广西E", "广西").replace("广西H", "广西").replace("湖北C", "湖北").replace("湖北D", "湖北").replace("山东C", "山东").replace("山东D", "山东").replace("山东E", "山东").replace("山东H", "山东").replace("安徽C", "安徽").replace("安徽D", "安徽").replace("安徽E", "安徽").replace("安徽H", "安徽").replace("江西C", "").replace("江西D", "").replace("江西E", "").replace("江西H", "").replace("江XB", "").replace("江西欢笑剧场", "欢笑剧场").replace("江西都市剧场", "都市剧场").replace("陕西C", "陕西").replace("陕西D", "陕西").replace("陕西E", "陕西").replace("陕西H", "陕西").replace("浙江C", "浙江").replace("浙江D", "浙江").replace("浙江E", "浙江").replace("浙江H", "浙江").replace("四川C", "四川").replace("四川D", "四川").replace("四川E", "四川").replace("四川H", "四川").replace("辽宁C", "辽宁").replace("辽宁D", "辽宁").replace("辽宁E", "辽宁").replace("辽宁H", "辽宁").replace("吉林C", "吉林").replace("山西C", "山西").replace("山西D", "山西").replace("山西E", "山西").replace("山西H", "山西").replace("CHE-V", "Channel-V").replace("爱上4", "爱上4K").replace("4超清", "4K超清").replace("凤凰卫视咨询台", "凤凰卫视资讯台").replace("CHC家庭电影", "CHC家庭影院").replace("CCTV怀旧剧场", "怀旧剧场").replace("CCTV文化精品", "文化精品").replace("CCTV第一剧场", "第一剧场").replace("CCTV高尔夫网球", "高尔夫网球")

with open('txt_files/AMER-delete.txt', 'w', encoding='utf-8') as file:
    file.write(content)
	
#enter
	
  ##################################################################################################################################SPLIT#
  

#enter
with open('txt_files/AMER-delete.txt', 'r', encoding="utf-8") as file:
 lines = file.readlines()
 
#enter
 unique_lines = [] 
 seen_lines = set() 

#enter
for line in lines:
 if line not in seen_lines:
  unique_lines.append(line)
  seen_lines.add(line)

#enter
with open('iptv.txt', 'w', encoding="utf-8") as file:
 file.writelines(unique_lines)

#enter

##################################################################################################################################SPLIT#

#enter

os.remove("txt_files/IP_addressjump.txt")

os.remove("txt_files/AMER-delete.txt")

os.remove("txt_files/AMER-start.txt")

os.remove("txt_files/merga.txt")

os.remove("txt_files/排序.txt")

os.remove("txt_files/T1.txt")

print("over")

with open('iptv.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

url_dict = defaultdict(list)

for line in lines:
    parts = line.strip().split(',', 1)
    if len(parts) == 2:
        name, url = parts
        url_dict[name].append(url)

with open('iptv.txt', 'w', encoding="utf-8") as file:
    for name, urls in url_dict.items():
        merged_url = f"{name}, {'#'.join(urls)}\n"
        file.write(merged_url)

print("Processing complete")
