import cv2 

import time

from datetime import datetime, timedelta

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
exclude_strings = ['121.207.104', 'xeace.cn:8888', '//27.10', '//220.176.218', '//171.221.129', '//118.122.111', '//27.191.71', '//175.11.171', '//220.176.218', '//117.43.80', '//182.139.152', '//118.122.111', '//118.112.60', '//27.191.71', '//122.232.188', '//125.71.44', '//122.234.77', '//122.232.188', '//14.105.105.35', '//27.191.71.248', '//144.255.40.160', '//140.250.221', '//223.242.146', '//182.139.215', '//182.150.168', '//120.32.11', '//113.86.204.209', '//110.185.44', '///61.157.92.168', '//59.56.214', '//117.25.38', '//125.82.171', '//117.12.148', '//183.5.92', '//117.66.231', '//36.47.83', '//115.221.95', '//113.120.108', '//115.193.167', '//117.28.112', '//117.25.38', '//117.67.169', '//221.15.251', '//117.67.169', '//221.15.251', '//116.5.168', '//175.0.95', '//118.248.154', '//220.175.144', '//118.254.201', '//14.154.192', '//124.112.208', '//182.148.30', '//110.185.70', '//183.5.97.206', '//123.55.112', '//222.182.115', '//14.117.233', '//113.13.242', '//59.56.214.134', '//58.42.184.132', '//58.42.184.132', '//220.192.1.40', '//27.11.253.19', '//27.11.58.239', '//14.105.104', '//183.54.208.185', '//116.252.77.132', '//221.232.175', '//144.255.44.24', '//113.222.42.190', '//61.150.11', '//110.185.10', '//118.254', '//122.232.188', '//171.116.157', '//125.43.40', '//125.86.181', '//27.153.80', '//61.190.129.1', '//182.46.8', '//119.130.11', '//58.63.65', '//1.84.218', '//183.184', '//171.217.81', '//27.190.83.', '//1.197.1', '//58.46.249', '//125.71.170', '//119.4.15', '//222.138.213', '//222.138.213', '//222.94.90', '//222.95.95', '//117.69', '//60.168.228', '//223.215.43', '//223.240.250', '//60.171.98', '//27.151.150', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+']

#enter
file_paths = ["北京联通.txt", "贵州电信.txt", "四川联通.txt", "河北电信.txt", "Sus.txt"]

#enter
with open("Kmerga2H+OLD.txt", "w", encoding="utf-8") as output:
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
with open('Kmerga2H+OLD.txt', 'r', encoding='utf-8') as file:
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
with open('Kmerga2H+OLD-SPD.txt', 'w', encoding='utf-8') as file:
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
exclude_strings = ['121.207.104', 'xeace.cn:8888', '//27.10', '//220.176.218', '//171.221.129', '//118.122.111', '//27.191.71', '//175.11.171', '//220.176.218', '//117.43.80', '//182.139.152', '//118.122.111', '//118.112.60', '//27.191.71', '//122.232.188', '//125.71.44', '//122.234.77', '//122.232.188', '//14.105.105.35', '//27.191.71.248', '//144.255.40.160', '//140.250.221', '//223.242.146', '//182.139.215', '//182.150.168', '//120.32.11', '//113.86.204.209', '//110.185.44', '///61.157.92.168', '//59.56.214', '//117.25.38', '//125.82.171', '//117.12.148', '//183.5.92', '//117.66.231', '//36.47.83', '//115.221.95', '//113.120.108', '//115.193.167', '//117.28.112', '//117.25.38', '//117.67.169', '//221.15.251', '//117.67.169', '//221.15.251', '//116.5.168', '//175.0.95', '//118.248.154', '//220.175.144', '//118.254.201', '//14.154.192', '//124.112.208', '//182.148.30', '//110.185.70', '//183.5.97.206', '//123.55.112', '//222.182.115', '//14.117.233', '//113.13.242', '//59.56.214.134', '//58.42.184.132', '//58.42.184.132', '//220.192.1.40', '//27.11.253.19', '//27.11.58.239', '//14.105.104', '//183.54.208.185', '//116.252.77.132', '//221.232.175', '//144.255.44.24', '//113.222.42.190', '//61.150.11', '//110.185.10', '//118.254', '//122.232.188', '//171.116.157', '//125.43.40', '//125.86.181', '//27.153.80', '//61.190.129.1', '//182.46.8', '//119.130.11', '//58.63.65', '//1.84.218', '//183.184', '//171.217.81', '//27.190.83.', '//1.197.1', '//58.46.249', '//125.71.170', '//119.4.15', '//222.138.213', '//222.138.213', '//222.94.90', '//222.95.95', '//117.69', '//60.168.228', '//223.215.43', '//223.240.250', '//60.171.98', '//27.151.150', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+']

#enter
file_paths = ["安徽电信.txt", "江苏电信.txt", "Susa.txt"]

#enter
with open("Kmergalow2H+lowOLD.txt", "w", encoding="utf-8") as output:
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
with open('Kmergalow2H+lowOLD.txt', 'r', encoding='utf-8') as file:
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
with open('Kmergalow2H+lowOLD-SPD.txt', 'w', encoding='utf-8') as file:
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
exclude_strings = ['121.207.104', 'xeace.cn:8888', '//27.10', '//220.176.218', '//171.221.129', '//118.122.111', '//27.191.71', '//175.11.171', '//220.176.218', '//117.43.80', '//182.139.152', '//118.122.111', '//118.112.60', '//27.191.71', '//122.232.188', '//125.71.44', '//122.234.77', '//122.232.188', '//14.105.105.35', '//27.191.71.248', '//144.255.40.160', '//140.250.221', '//223.242.146', '//182.139.215', '//182.150.168', '//120.32.11', '//113.86.204.209', '//110.185.44', '///61.157.92.168', '//59.56.214', '//117.25.38', '//125.82.171', '//117.12.148', '//183.5.92', '//117.66.231', '//36.47.83', '//115.221.95', '//113.120.108', '//115.193.167', '//117.28.112', '//117.25.38', '//117.67.169', '//221.15.251', '//117.67.169', '//221.15.251', '//116.5.168', '//175.0.95', '//118.248.154', '//220.175.144', '//118.254.201', '//14.154.192', '//124.112.208', '//182.148.30', '//110.185.70', '//183.5.97.206', '//123.55.112', '//222.182.115', '//14.117.233', '//113.13.242', '//59.56.214.134', '//58.42.184.132', '//58.42.184.132', '//220.192.1.40', '//27.11.253.19', '//27.11.58.239', '//14.105.104', '//183.54.208.185', '//116.252.77.132', '//221.232.175', '//144.255.44.24', '//113.222.42.190', '//61.150.11', '//110.185.10', '//118.254', '//122.232.188', '//171.116.157', '//125.43.40', '//125.86.181', '//27.153.80', '//61.190.129.1', '//182.46.8', '//119.130.11', '//58.63.65', '//1.84.218', '//183.184', '//171.217.81', '//27.190.83.', '//1.197.1', '//58.46.249', '//125.71.170', '//119.4.15', '//222.138.213', '//222.138.213', '//222.94.90', '//222.95.95', '//117.69', '//60.168.228', '//223.215.43', '//223.240.250', '//60.171.98', '//27.151.150', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+', '//+']

#enter
file_paths = ["四川电信.txt", "江西电信.txt", "Susaw.txt"]

#enter
with open("Kmergaverylow2H+verylowOLD.txt", "w", encoding="utf-8") as output:
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
with open('Kmergaverylow2H+verylowOLD.txt', 'r', encoding='utf-8') as file:
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
with open('Kmergaverylow2H+verylowOLD-SPD.txt', 'w', encoding='utf-8') as file:
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
with open('set.txt', 'r', encoding='utf-8') as file:
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
with open('JX-LOW-SPD.txt', 'w', encoding='utf-8') as file:
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
with open('setr.txt', 'r', encoding='utf-8') as file:
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
with open('gaar-SPD.txt', 'w', encoding='utf-8') as file:
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
with open('Kmerga2H+OLD-SPD.txt', 'r', encoding='utf-8') as file_in:
    #enter
    with open('Kmerga2H+OLD-SPDjump.txt', 'w', encoding='utf-8') as file_out:
        #enter
        for line in file_in:
            #enter
            file_out.write(line)

# enter
#enter
seen_lines = set()

#enter
with open('Kmerga2H+OLD-SPDjump.txt', 'r', encoding='utf-8') as file_in, \
     open('Sus.txt', 'w', encoding='utf-8') as file_out:
    #enter文件
    for line in file_in:
        #enter
        stripped_line = line.strip()
        if stripped_line not in seen_lines:
            #enter
            file_out.write(line)
            seen_lines.add(stripped_line)
			
			

#enter
with open('Kmergalow2H+lowOLD-SPD.txt', 'r', encoding='utf-8') as file_in:
    #enter
    with open('Kmergalow2H+lowOLD-SPDjump.txt', 'w', encoding='utf-8') as file_out:
        #enter
        for line in file_in:
            #enter
            file_out.write(line)

# enter
#enter
seen_lines = set()

#enter
with open('Kmergalow2H+lowOLD-SPDjump.txt', 'r', encoding='utf-8') as file_in, \
     open('Susa.txt', 'w', encoding='utf-8') as file_out:
    #enter文件
    for line in file_in:
        #enter
        stripped_line = line.strip()
        if stripped_line not in seen_lines:
            #enter
            file_out.write(line)
            seen_lines.add(stripped_line)


#enter
with open('Kmergaverylow2H+verylowOLD-SPD.txt', 'r', encoding='utf-8') as file_in:
    #enter
    with open('Kmergaverylow2H+verylowOLD-SPDjump.txt', 'w', encoding='utf-8') as file_out:
        #enter
        for line in file_in:
            #enter
            file_out.write(line)

# enter
#enter
seen_lines = set()

#enter
with open('Kmergaverylow2H+verylowOLD-SPDjump.txt', 'r', encoding='utf-8') as file_in, \
     open('Susaw.txt', 'w', encoding='utf-8') as file_out:
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
with open('IP address.txt', 'a', encoding='utf-8') as file:
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

with open('Kmerga2H+OLD.txt', 'r', encoding='utf-8') as file, open('IP address.txt', 'a', encoding='utf-8') as IP_save:

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         IP_save.write(line)  #go
		 
		 
#enter
#enter		 
keywords = ['S川A爱科幻','天JD都市高清','安HH生活时尚','山DB农科','山XD都市剧场','广DA经济科教','广XH南宁都市','江S南京生活','江XB都市剧场','河BA农民高清','河N民生频道','河NC电视剧频道','浙JC教育高清','湖N常德新闻','福JA少儿','辽LD沈阳新闻','重QD影视频道','陕XA新闻资讯']  
pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter	 
with open('Kmergalow2H+lowOLD.txt', 'r', encoding='utf-8') as file, open('IP address.txt', 'a', encoding='utf-8') as IP_save:

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         IP_save.write(line)  #enter 
		 
		 
		 
		 
#enter
#enter		 
keywords = ['S川A爱科幻','天JD都市高清','安HH生活时尚','山DB农科','山XD都市剧场','广DA经济科教','广XH南宁都市','江S南京生活','江XB都市剧场','河BA农民高清','河N民生频道','河NC电视剧频道','浙JC教育高清','湖N常德新闻','福JA少儿','辽LD沈阳新闻','重QD影视频道','陕XA新闻资讯']  
pattern = '|'.join(keywords)  #enterenter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter	 
with open('Kmergaverylow2H+verylowOLD.txt', 'r', encoding='utf-8') as file, open('IP address.txt', 'a', encoding='utf-8') as IP_save:

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         IP_save.write(line)  #enter 		 

#########################split##



#enter
with open('IP address.txt', 'r', encoding='utf-8') as file_in:
    # go
    with open('IP_savejump.txt', 'w', encoding='utf-8') as file_out:
        #enterIP address.txt
        for line in file_in:
            #enterIP_savejump.txt
            file_out.write(line)

# enter
#enter
seen_lines = set()

#enter
with open('IP_savejump.txt', 'r', encoding='utf-8') as file_in, \
     open('IP address.txt', 'w', encoding='utf-8') as file_out:
    #enter IP_savejump.txt
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
file_paths = ['Sus.txt','Susa.txt','Susaw.txt','JX-LOW-SPD.txt','gaar-SPD.txt',"ga"]



for file_path in file_paths:

    with open(file_path, 'r', encoding="utf-8") as file:

        content = file.read()

        file_contents.append(content)


#enter

with open("merga.txt", "w", encoding="utf-8") as output:

    output.write('\n'.join(file_contents))


#替换

for line in fileinput.input("merga.txt", inplace=True):  #enter

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

    line = line.replace("CCTV4国际", "CCTV4")

    line = line.replace("CCTV4中文国际", "CCTV4")

    line = line.replace("CCTV4欧洲", "CCTV4")

    line = line.replace("CCTV5体育", "CCTV5")

    line = line.replace("CCTV5+体育", "CCTV5+")

    line = line.replace("CCTV6电影", "CCTV6")

    line = line.replace("CCTV7军事", "CCTV7")

    line = line.replace("CCTV7军农", "CCTV7")

    line = line.replace("CCTV7农业", "CCTV7")

    line = line.replace("CCTV7国防军事", "CCTV7")

    line = line.replace("CCTV8电视剧", "CCTV8")

    line = line.replace("CCTV8纪录", "CCTV9")

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

for line in fileinput.input("merga.txt", inplace=True):  #enter

    
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



with open('merga.txt', 'r', encoding='utf-8') as f:

    lines = f.readlines()


lines.sort()


with open('排序.txt', 'w', encoding='UTF-8') as f:

    for line in lines:

        f.write(line)


#enter##########################################################################################################################

for line in fileinput.input("排序.txt", inplace=True):  #enter

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
with open('g.txt', 'r', encoding='utf-8') as file1:
  
    #enter
    with open('TT1.txt', 'w', encoding='utf-8') as file2:
        #enter
        for line in file1:
            #enter
            file2.write(line)


#star#########################
#enter#############################################################################################

keywords = ['CCTV','CETV', 'CF', 'IPT淘', 'CHC', 'IWA', '凤凰卫视', '星空', 'CHANNEL-V', '卫视', '金鹰卡通', '纪实科教', '卡酷少儿', '嘉佳卡通', '哈哈炫动', '乐游频道', '动漫秀场', '新动漫','纪实人文', '金色学堂',  '纪实科教', '金鹰纪实', '求索记录']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T1.txt', 'w', encoding='utf-8') as T1:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T1.write(line)  #enter

for line in fileinput.input("T1.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter
with open('TT1.txt', 'a', encoding='utf-8') as TT1:    #####enter

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

with open('T1.txt', 'r', encoding="utf-8") as input_file, open('TT1.txt', 'a', encoding="utf-8") as output_file:
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



keywords = ['重Q']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T5.txt', 'w', encoding='utf-8') as T5:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T5.write(line)  #enter

for line in fileinput.input("T5.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT5.txt', 'w', encoding='utf-8') as TT5:    #####enter

    TT5.write('\n👑重庆数字高清,#genre#\n')        
 
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

with open('T5.txt', 'r', encoding="utf-8") as input_file, open('TT5.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['北J']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T6.txt', 'w', encoding='utf-8') as T6:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T6.write(line)  #enter

for line in fileinput.input("T6.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT6.txt', 'w', encoding='utf-8') as TT6:    #####enter

    TT6.write('\n👑北京数字高清,#genre#\n')        
 
    print(line, end="")  #enter 
#enter

#enter
import re

##enter
def custom_sort_key(item):
    channel, url = item.split(',')

    #enter
    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))
    channel_sort_key = (channel_letters, int(channel_numbers) if channel_numbers.isdigit() else 0)

    #enter
    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    #enter
    if sort_key[0].isalpha():
        #enter
        #enter
        sort_key = (-1, sort_key[::-1])
    elif sort_key.isdigit():
        #enter
        sort_key = (1, -int(sort_key))
    else:
        #enter
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T6.txt', 'r', encoding="utf-8") as input_file, open('TT6.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['河B']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T7.txt', 'w', encoding='utf-8') as T7:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T7.write(line)  #enter

for line in fileinput.input("T7.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT7.txt', 'w', encoding='utf-8') as TT7:    #####enter

    TT7.write('\n👑河北数字高清,#genre#\n')        
 
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
        sort_key = (1, int(sort_key))  #enter-
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T7.txt', 'r', encoding="utf-8") as input_file, open('TT7.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['河N']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T8.txt', 'w', encoding='utf-8') as T8:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T8.write(line)  #enter

for line in fileinput.input("T8.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT8.txt', 'w', encoding='utf-8') as TT8:    #####enter

    TT8.write('\n👑河南数字高清,#genre#\n')        
 
    print(line, end="")  #enter 
#enter

#enter
import re

# enter
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

with open('T8.txt', 'r', encoding="utf-8") as input_file, open('TT8.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['天J']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T9.txt', 'w', encoding='utf-8') as T9:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T9.write(line)  #enter

for line in fileinput.input("T9.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT9.txt', 'w', encoding='utf-8') as TT9:    #####enter

    TT9.write('\n👑天津数字高清,#genre#\n')        
 
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
        sort_key = (1, int(sort_key))  #enter-
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T9.txt', 'r', encoding="utf-8") as input_file, open('TT9.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['广D']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T10.txt', 'w', encoding='utf-8') as T10:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T10.write(line)  #enter

for line in fileinput.input("T10.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT10.txt', 'w', encoding='utf-8') as TT10:    #####enter

    TT10.write('\n👑广东数字高清,#genre#\n')        
 
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

with open('T10.txt', 'r', encoding="utf-8") as input_file, open('TT10.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['广X']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T11.txt', 'w', encoding='utf-8') as T11:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T11.write(line)  #enter

for line in fileinput.input("T11.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT11.txt', 'w', encoding='utf-8') as TT11:    #####enter

    TT11.write('\n👑广西数字高清,#genre#\n')        
 
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
        sort_key = (1, int(sort_key))  #enter-
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T11.txt', 'r', encoding="utf-8") as input_file, open('TT11.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['湖B']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T12.txt', 'w', encoding='utf-8') as T12:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T12.write(line)  #enter

for line in fileinput.input("T12.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT12.txt', 'w', encoding='utf-8') as TT12:    #####enter

    TT12.write('\n👑湖北数字高清,#genre#\n')        
 
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

with open('T12.txt', 'r', encoding="utf-8") as input_file, open('TT12.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['山DA','山DB','山DC','山DD','山DE','山DF','山DG','山DK','山DZ']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T13.txt', 'w', encoding='utf-8') as T13:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T13.write(line)  #enter

for line in fileinput.input("T13.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT13.txt', 'w', encoding='utf-8') as TT13:    #####enter

    TT13.write('\n👑山东数字高清,#genre#\n')        
 
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

with open('T13.txt', 'r', encoding="utf-8") as input_file, open('TT13.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['安H']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T14.txt', 'w', encoding='utf-8') as T14:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T14.write(line)  #enter

for line in fileinput.input("T14.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT14.txt', 'w', encoding='utf-8') as TT14:    #####enter

    TT14.write('\n👑安徽数字高清,#genre#\n')        
 
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
        sort_key = (1, -int(sort_key))  #enter-
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T14.txt', 'r', encoding="utf-8") as input_file, open('TT14.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['江S']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T15.txt', 'w', encoding='utf-8') as T15:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T15.write(line)  #enter

for line in fileinput.input("T15.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT15.txt', 'w', encoding='utf-8') as TT15:    #####enter

    TT15.write('\n👑江苏数字高清,#genre#\n')        
 
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

with open('T15.txt', 'r', encoding="utf-8") as input_file, open('TT15.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['江XA','江XB','江XC','江XD','江XE','江X']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T16.txt', 'w', encoding='utf-8') as T16:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T16.write(line)  #enter

for line in fileinput.input("T16.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT16.txt', 'w', encoding='utf-8') as TT16:    #####enter

    TT16.write('\n👑江西数字高清,#genre#\n')        
 
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

with open('T16.txt', 'r', encoding="utf-8") as input_file, open('TT16.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['山X']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T17.txt', 'w', encoding='utf-8') as T17:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T17.write(line)  #enter

for line in fileinput.input("T17.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT17.txt', 'w', encoding='utf-8') as TT17:    #####enter

    TT17.write('\n👑山西数字高清,#genre#\n')        
 
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

with open('T17.txt', 'r', encoding="utf-8") as input_file, open('TT17.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['浙J']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T18.txt', 'w', encoding='utf-8') as T18:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T18.write(line)  #enter

for line in fileinput.input("T18.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT18.txt', 'w', encoding='utf-8') as TT18:    #####enter

    TT18.write('\n👑浙江数字高清,#genre#\n')        
 
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

with open('T18.txt', 'r', encoding="utf-8") as input_file, open('TT18.txt', 'a', encoding="utf-8") as output_file:
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
   # enter
with open('setra.txt', 'r', encoding='utf-8') as file1:
  
    #enter
    with open('TT19.txt', 'w', encoding='utf-8') as file2:
        #enter
        for line in file1:
            #enter
            file2.write(line)
   
   
#star#########################
#enter#############################################################################################

keywords = ['湖N']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T19.txt', 'w', encoding='utf-8') as T19:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T19.write(line)  #enter

for line in fileinput.input("T19.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT19.txt', 'a', encoding='utf-8') as TT19:    #####enter

    TT19.write('\n以上手工录入\n')        
 
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

with open('T19.txt', 'r', encoding="utf-8") as input_file, open('TT19.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['辽L']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T20.txt', 'w', encoding='utf-8') as T20:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T20.write(line)  #enter

for line in fileinput.input("T20.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT20.txt', 'w', encoding='utf-8') as TT20:    #####enter

    TT20.write('\n👑辽宁数字高清,#genre#\n')        
 
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
        sort_key = (1, int(sort_key))  #enter-
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T20.txt', 'r', encoding="utf-8") as input_file, open('TT20.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['吉L','黑龙江']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T21.txt', 'w', encoding='utf-8') as T21:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T21.write(line)  #enter

for line in fileinput.input("T21.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT21.txt', 'w', encoding='utf-8') as TT21:    #####enter

    TT21.write('\n👑吉林黑龙江频道,#genre#\n')        
 
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

with open('T21.txt', 'r', encoding="utf-8") as input_file, open('TT21.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['贵Z','习水']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T22.txt', 'w', encoding='utf-8') as T22:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T22.write(line)  #enter

for line in fileinput.input("T22.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT22.txt', 'w', encoding='utf-8') as TT22:    #####enter

    TT22.write('\n👑贵州地方频道,#genre#\n')        
 
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

with open('T22.txt', 'r', encoding="utf-8") as input_file, open('TT22.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['陕X']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T23.txt', 'w', encoding='utf-8') as T23:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T23.write(line)  #enter

for line in fileinput.input("T23.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT23.txt', 'w', encoding='utf-8') as TT23:    #####enter

    TT23.write('\n👑陕西数字高清,#genre#\n')        
 
    print(line, end="")  #enter 
#enter

#enter
import re

# enter
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
        sort_key = (1, int(sort_key))  #enter-
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T23.txt', 'r', encoding="utf-8") as input_file, open('TT23.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['新J']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T24.txt', 'w', encoding='utf-8') as T24:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T24.write(line)  #enter

for line in fileinput.input("T24.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT24.txt', 'w', encoding='utf-8') as TT24:    #####enter

    TT24.write('\n👑新疆数字高清,#genre#\n')        
 
    print(line, end="")  #enter 
#enter

#enter
import re

# enter
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

with open('T24.txt', 'r', encoding="utf-8") as input_file, open('TT24.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['S川']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T25.txt', 'w', encoding='utf-8') as T25:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T25.write(line)  #enter

for line in fileinput.input("T25.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT25.txt', 'w', encoding='utf-8') as TT25:    #####enter

    TT25.write('\n👑四川数字高清,#genre#\n')        
 
    print(line, end="")  #enter 
#enter

#enter
import re

# enter
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

with open('T25.txt', 'r', encoding="utf-8") as input_file, open('TT25.txt', 'a', encoding="utf-8") as output_file:
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

keywords = ['福JA','福JB','福JC','福J']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T26.txt', 'w', encoding='utf-8') as T26:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T26.write(line)  #enter

for line in fileinput.input("T26.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT26.txt', 'w', encoding='utf-8') as TT26:    #####enter

    TT26.write('\n👑福建数字高清,#genre#\n')        
 
    print(line, end="")  #enter 
#enter

#enter
import re

# enter
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

with open('T26.txt', 'r', encoding="utf-8") as input_file, open('TT26.txt', 'a', encoding="utf-8") as output_file:
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
#star#########################
#enter#############################################################################################

keywords = ['宁夏','青海']  #enter

pattern = '|'.join(keywords)  #enter

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #enter

with open('排序.txt', 'r', encoding='utf-8') as file, open('T27.txt', 'w', encoding='utf-8') as T27:    #####enter

    for line in file:

        if re.search(pattern, line) and line.count(',') == 1:  #enter

         T27.write(line)  #enter

for line in fileinput.input("T27.txt", inplace=True):  #enter 

    print(line, end="")  #enter          

#enter-genre###################
with open('TT27.txt', 'w', encoding='utf-8') as TT27:    #####enter

    TT27.write('\n👑宁夏青海地方,#genre#\n')        
 
    print(line, end="")  #enter 
#enter

#enter
import re

# enter
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

with open('T27.txt', 'r', encoding="utf-8") as input_file, open('TT27.txt', 'a', encoding="utf-8") as output_file:
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

#starmerga多个文件到一个文件###########

file_contents = []

file_paths = ["TT1.txt", "TT2.txt", "TT4.txt", "TT5.txt", "TT6.txt", "TT7.txt", "TT8.txt", "TT9.txt", "TT10.txt", "TT11.txt", "TT12.txt", "TT13.txt", "TT14.txt", "TT15.txt", "TT16.txt", "TT17.txt", "TT18.txt", "TT19.txt", "TT20.txt", "TT21.txt", "TT22.txt", "TT23.txt", "TT24.txt", "TT25.txt", "TT26.txt",'TT27.txt'] 

for file_path in file_paths:

    with open(file_path, 'r', encoding="utf-8") as file:

        content = file.read()

        file_contents.append(content)



# enter

with open("AMER-start.txt", "w", encoding="utf-8") as output:

    output.write('\n'.join(file_contents))

#enter
##################################################################################################################################SPLIT#
  
  

#star
with open('AMER-start.txt', 'r', encoding='utf-8') as file:
    content = file.read()

#enter
content = content.replace("WA", "").replace("WP", "").replace("WB", "").replace("WC", "").replace("WD", "").replace("WE", "").replace("WF", "").replace("WG", "").replace("WH", "").replace("WI", "").replace("WJ", "").replace("WK", "").replace("WL", "").replace("WM", "").replace("WN", "").replace("WO", "").replace("WP", "").replace("WQ", "").replace("WR", "").replace("WS", "").replace("WT", "").replace("WU", "").replace("WV", "").replace("WW", "").replace("WX", "").replace("WY", "").replace("WZ", "").replace("CF", "").replace("IV", "").replace("X纪实", "X纪实").replace("Y卡酷", "卡酷").replace("Y动漫", "动漫").replace("Y金色学堂", "金色学堂").replace("电Y", "电影").replace("老DY", "老电影").replace("X乐", "乐").replace("X求", "求").replace("X纪", "纪").replace("X记", "记").replace("X金", "金").replace("Y动", "动").replace("Y卡", "卡").replace("Y咔", "咔").replace("Y嘉", "嘉").replace("Y新", "新").replace("剧J", "连续剧").replace("重Q", "重庆").replace("北J", "北京").replace("河B", "河北").replace("河N", "河南").replace("天J", "天津").replace("湖B", "湖北").replace("湖N", "湖南").replace("山D", "山东").replace("安H", "安徽").replace("江S", "江苏").replace("山X", "山西").replace("浙J", "浙江").replace("辽L", "辽宁").replace("吉L", "吉林").replace("贵Z", "贵州").replace("陕X", "陕西").replace("S川", "四川").replace("褔J", "福建").replace("GAT-", "").replace("裾J", "裾集").replace("江X", "江西").replace("新J", "新疆").replace("褔JA", "福建").replace("褔JB", "福建").replace("褔JC", "福建").replace("褔JD", "福建").replace("福J", "福建").replace("广X", "广西").replace("A", "").replace("B", "").replace("F", "").replace("G", "").replace("I", "").replace("J", "").replace("K", "").replace("L", "").replace("M", "").replace("N", "").replace("O", "").replace("P", "").replace("Q", "").replace("R", "").replace("S", "").replace("U", "").replace("W", "").replace("X", "").replace("Y", "").replace("Z", "").replace("C新闻", "新闻").replace("电映C", "电映").replace("电映E", "电映").replace("电映H", "电映").replace("D影视", "影视").replace("E都市", "都市").replace("H新农", "新农").replace("河北C", "河北").replace("河北D", "河北").replace("河南C", "河南").replace("河南D", "河南").replace("天津C", "天津").replace("天津D", "天津").replace("天津E", "天津").replace("广D", "广东").replace("广东C", "广东").replace("广东H", "广东").replace("广西C", "广西").replace("广西D", "广西").replace("广西E", "广西").replace("广西H", "广西").replace("湖北C", "湖北").replace("湖北D", "湖北").replace("山东C", "山东").replace("山东D", "山东").replace("山东E", "山东").replace("山东H", "山东").replace("安徽C", "安徽").replace("安徽D", "安徽").replace("安徽E", "安徽").replace("安徽H", "安徽").replace("江西C", "江西").replace("江西D", "江西").replace("江西E", "江西").replace("江西H", "江西").replace("陕西C", "陕西").replace("陕西D", "陕西").replace("陕西E", "陕西").replace("陕西H", "陕西").replace("浙江C", "浙江").replace("浙江D", "浙江").replace("浙江E", "浙江").replace("浙江H", "浙江").replace("四川C", "四川").replace("四川D", "四川").replace("四川E", "四川").replace("四川H", "四川").replace("辽宁C", "辽宁").replace("辽宁D", "辽宁").replace("辽宁E", "辽宁").replace("辽宁H", "辽宁").replace("吉林C", "吉林").replace("山西C", "山西").replace("山西D", "山西").replace("山西E", "山西").replace("山西H", "山西").replace("少_儿", "少儿").replace("少*儿", "少儿")

with open('AMER-delete.txt', 'w', encoding='utf-8') as file:
    file.write(content)
	
#enter
	
  ##################################################################################################################################SPLIT#
  

#enter
with open('AMER-delete.txt', 'r', encoding="utf-8") as file:
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
with open('gotostill.txt', 'w', encoding="utf-8") as file:
 file.writelines(unique_lines)

#enter

##################################################################################################################################SPLIT#

#enter

os.remove("IP_savejump.txt")

os.remove("AMER-delete.txt")

os.remove("AMER-start.txt")

os.remove("merga.txt")

os.remove("排序.txt")

os.remove("T1.txt")

os.remove("T2.txt")

os.remove("T4.txt")

os.remove("T5.txt")

os.remove("T6.txt")

os.remove("T7.txt")

os.remove("T8.txt")

os.remove("T9.txt")

os.remove("T10.txt")

os.remove("T11.txt")

os.remove("T12.txt")

os.remove("T13.txt")

os.remove("T14.txt")

os.remove("T15.txt")

os.remove("T16.txt")

os.remove("T17.txt")

os.remove("T18.txt")

os.remove("T19.txt")

os.remove("T20.txt")

os.remove("T21.txt")

os.remove("T22.txt")

os.remove("T23.txt")

os.remove("T24.txt")

os.remove("T25.txt")

os.remove("T26.txt")

os.remove("T27.txt")

os.remove("TT1.txt")

os.remove("TT2.txt")

os.remove("TT4.txt")

os.remove("TT5.txt")

os.remove("TT6.txt")

os.remove("TT7.txt")

os.remove("TT8.txt")

os.remove("TT9.txt")

os.remove("TT10.txt")

os.remove("TT11.txt")

os.remove("TT12.txt")

os.remove("TT13.txt")

os.remove("TT14.txt")

os.remove("TT15.txt")

os.remove("TT16.txt")

os.remove("TT17.txt")

os.remove("TT18.txt")

os.remove("TT19.txt")

os.remove("TT20.txt")

os.remove("TT21.txt")

os.remove("TT22.txt")

os.remove("TT23.txt")

os.remove("TT24.txt")

os.remove("TT25.txt")

os.remove("TT26.txt")

os.remove("TT27.txt")

print("over")
