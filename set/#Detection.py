import cv2
import time

tested_ips = {}

with open('txt_files/M-SPD_TST.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.count(',') == 1:
            channel = line.strip()
            
            ip_start = line.find(',') + 1
            rtp_pos = line.find('rtp')
            if rtp_pos != -1:
                ip_part = line[ip_start:rtp_pos].strip()
            
            url_start = ip_start
            url_end = line.find('$')
            if url_end != -1:
                url = line[url_start:url_end].strip()
            else:
                url = line[url_start:].strip()

            if ip_part in tested_ips:
                print(f"JUMP IP: {ip_part}")
                continue

            cap = cv2.VideoCapture(url)
            
            start_time = time.time()
            frame_count = 0
            
            while frame_count < 9999 and (time.time() - start_time) < 10:  # 超时时间
                ret, frame = cap.read()
                if not ret:
                    break
                frame_count += 1

            end_time = time.time()
            total_time = end_time - start_time

            if frame_count > 2:
                tested_ips[ip_part] = {'status': 'ok', 'frames': frame_count, 'time': total_time}
            else:
                tested_ips[ip_part] = {'status': 'tested', 'frames': frame_count, 'time': total_time}

            cap.release()

with open('txt_files/M-SPD_OUT.txt', 'w', encoding='utf-8') as file:
    with open('txt_files/M-SPD_TST.txt', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            if line.count(',') == 1:
                ip_start = line.find(',') + 1
                rtp_pos = line.find('rtp')
                if rtp_pos != -1:
                    ip_part = line[ip_start:rtp_pos].strip()
                else:
                    ip_part = line[ip_start:].strip()

                if ip_part in tested_ips and tested_ips[ip_part]['status'] == 'ok':
                    result_line = line.strip() + f"SPD{tested_ips[ip_part]['frames']}"
                    file.write(result_line + '\n')
