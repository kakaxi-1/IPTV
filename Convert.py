import os

# 定义分类规则
cctv_main_channels = ['CCTV1']
cctv_other_channels = ['CCTV2', 'CCTV3', 'CCTV4', 'CCTV4欧', 'CCTV4美', 'CCTV5', 'CCTV5+', 'CCTV6', 'CCTV7', 'CCTV8', 'CCTV9']
cctv_grouped_channels = ['CCTV10', 'CCTV11', 'CCTV12', 'CCTV13', 'CCTV14', 'CCTV15', 'CCTV17']
other_cctv_channels = [
    "文化精品", "央视台球", "风云音乐", "第一剧场", "风云剧场", "怀旧剧场", "女性时尚", 
    "高尔夫网球", "风云足球", "电视指南", "世界地理", "兵器科技", "CETV1", "CETV2", "CETV4", "CETV5"
]
satellite_channels = [
    '湖南卫视', '浙江卫视', '江苏卫视', '东方卫视', '深圳卫视', '广东卫视', '广西卫视', '东南卫视', '海南卫视', '北京卫视', '河北卫视',
    '河南卫视', '湖北卫视', '江西卫视', '四川卫视', '重庆卫视', '贵州卫视', '云南卫视', '天津卫视', '安徽卫视', '山东卫视', '辽宁卫视',
    '黑龙江卫视', '吉林卫视', '宁夏卫视', '山西卫视', '陕西卫视', '甘肃卫视', '青海卫视', '新疆卫视', '西藏卫视', '内蒙古卫视', '三沙卫视', '康巴卫视'
]
digital_channels = [
    '家庭影院', '动作电影', '高清电影', '淘电影', '淘剧场', '淘娱乐', '淘贝比', '淘萌宠', '凤凰卫视中文台', '凤凰卫视咨询台',
    '凤凰卫视电影台', '星空卫视', 'CHE-V', '动漫秀场', '生活时尚', '欢笑剧场', '都市剧场', '纪实人文', '金鹰纪实', '求索记录', 
    '睛彩竞技', '睛彩篮球', '睛彩羽毛球', '睛彩广场舞', '睛彩河北', '睛彩四川', '爱上4', '4超清', '乐游频道'
]

def read_iptv_file(filepath):
    """读取iptv.txt文件内容"""
    if not os.path.exists(filepath):
        print(f"文件 {filepath} 不存在。")
        return []

    with open(filepath, 'r', encoding='utf-8') as file:
        return file.readlines()

def classify_channels(lines):
    """对IPTV频道内容进行分类"""
    cctv_main_dict = {channel: [] for channel in cctv_main_channels}
    cctv_other_dict = {channel: [] for channel in cctv_other_channels}
    cctv_grouped_dict = {channel: [] for channel in cctv_grouped_channels + other_cctv_channels}
    satellite_list = []
    digital_list = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 分类CCTV1
        for cctv in cctv_main_channels:
            if cctv in line:
                cctv_main_dict[cctv].append(line)
                break
        # 分类CCTV2-CCTV9
        else:
            for cctv in cctv_other_channels:
                if cctv in line:
                    cctv_other_dict[cctv].append(line)
                    break
            # 分类CCTV10-CCTV17
            else:
                for cctv in cctv_grouped_channels:
                    if cctv in line:
                        cctv_grouped_dict[cctv].append(line)
                        break
                # 分类其他央视频道
                else:
                    for key in other_cctv_channels:
                        if key in line:
                            cctv_grouped_dict[key].append(line)
                            break
                    else:
                        # 分类卫视频道
                        if any(sat in line for sat in satellite_channels):
                            satellite_list.append(line)
                        # 分类数字频道
                        elif any(dig in line for dig in digital_channels):
                            digital_list.append(line)

    return cctv_main_dict, cctv_other_dict, cctv_grouped_dict, satellite_list, digital_list

def write_zubo_file(output_file, cctv_main_dict, cctv_other_dict, cctv_grouped_dict, satellite_list, digital_list):
    """将分类后的频道信息写入到zubo.txt"""
    with open(output_file, 'w', encoding='utf-8') as file:
        # 写入CCTV1分类
        file.write("央视,#genre#\n")
        for cctv in cctv_main_channels:
            if cctv_main_dict[cctv]:
                for line in cctv_main_dict[cctv]:
                    file.write(line + '\n')

        # 写入CCTV2-CCTV9分类
        for cctv in cctv_other_channels:
            if cctv_other_dict[cctv]:
                for line in cctv_other_dict[cctv]:
                    file.write(line + '\n')

        # 写入CCTV10-CCTV17和其他央视分类
        for cctv in cctv_grouped_channels + other_cctv_channels:
            if cctv_grouped_dict[cctv]:
                for line in cctv_grouped_dict[cctv]:
                    file.write(line + '\n')

        # 写入卫视频道
        file.write("卫视,#genre#\n")
        for line in satellite_list:
            file.write(line + '\n')

        # 写入数字频道
        file.write("数字,#genre#\n")
        for line in digital_list:
            file.write(line + '\n')

def main():
    iptv_file = "iptv.txt"
    zubo_file = "zubo.txt"

    lines = read_iptv_file(iptv_file)
    if not lines:
        return

    cctv_main_dict, cctv_other_dict, cctv_grouped_dict, satellite_list, digital_list = classify_channels(lines)
    write_zubo_file(zubo_file, cctv_main_dict, cctv_other_dict, cctv_grouped_dict, satellite_list, digital_list)

if __name__ == "__main__":
    main()
