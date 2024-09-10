import xml.etree.ElementTree as ET

def merge_xml_files(files):
    try:
        root = None
        for file in files:
            # 读取文件时指定编码
            with open(file, 'r', encoding='utf-8') as f:
                tree = ET.parse(f)
                if root is None:
                    root = tree.getroot()
                else:
                    root.extend(tree.getroot())

        # 输出合并后的 XML 文件，指定编码
        tree = ET.ElementTree(root)
        with open('epg.xml', 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
            
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# 使用文件名列表调用函数
merge_xml_files(["e.xml", "epg_part.xml"])
