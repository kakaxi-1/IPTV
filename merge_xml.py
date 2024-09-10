import xml.etree.ElementTree as ET

# 加载第一个XML文件
tree1 = ET.parse('e.xml')
root1 = tree1.getroot()

# 加载第二个XML文件
tree2 = ET.parse('epg_part.xml')
root2 = tree2.getroot()

# 将第二个XML文件的内容添加到第一个XML的根节点下
for elem in root2:
    root1.append(elem)

# 保存合并后的XML文件
tree1.write('epg.xml')
