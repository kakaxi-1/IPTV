

#SPD


import cv2
import time

#SPD
#SPD
tested_ips = {}

#SPD
with open('M-SPD_TST.txt', 'r', encoding='utf-8') as file:
    for line in file:
        #SPD
        if line.count(',') == 1:
            #SPD
            channel = line.strip()
            
            #SPD
            ip_start = line.find(',') + 1
            rtp_pos = line.find('rtp')
            if rtp_pos != -1:
                ip_part = line[ip_start:rtp_pos].strip()
            
            url_start = ip_start
            url_end = line.find('$')
            if url_end != -1:
                url = line[url_start:url_end].strip()
            else:
                #SPD
                url = line[url_start:].strip()
            

            #SPD
            if ip_part in tested_ips:
                #SPD
                print(f"JUMP IP: {ip_part}")
                continue

            #SPD
            cap = cv2.VideoCapture(url)
            
            #SPD
            start_time = time.time()
            frame_count = 0
            
            #SPD
            while frame_count < 9999 and (time.time() - start_time) < 10:  # 超时时间
                ret, frame = cap.read()
                if not ret:  #SPD
                    break  #SPD
                frame_count += 1  # SPD

            #SPD
            end_time = time.time()
            total_time = end_time - start_time

            #SPD
            if frame_count > 2:  #SPD
                tested_ips[ip_part] = {'status': 'ok', 'frames': frame_count, 'time': total_time}
            else:
                #SPD
                tested_ips[ip_part] = {'status': 'tested', 'frames': frame_count, 'time': total_time}

            # SPD
            cap.release()

#SPD
with open('M-SPD_OUT.txt', 'w', encoding='utf-8') as file:
    with open('M-SPD_TST.txt', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            #SPD
            if line.count(',') == 1:
                #SPD
                ip_start = line.find(',') + 1
                rtp_pos = line.find('rtp')
                if rtp_pos != -1:
                    ip_part = line[ip_start:rtp_pos].strip()
                else:
                    ip_part = line[ip_start:].strip()  #SPD

                #SPD
                if ip_part in tested_ips and tested_ips[ip_part]['status'] == 'ok':
                    #SPD
                    result_line = line.strip() + f"SPD{tested_ips[ip_part]['frames']}"
                    file.write(result_line + '\n')
