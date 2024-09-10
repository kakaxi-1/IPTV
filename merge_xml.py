import xml.etree.ElementTree as ET

tree1 = ET.parse('e.xml')
root1 = tree1.getroot()

tree2 = ET.parse('epg_part.xml')
root2 = tree2.getroot()

for elem in root2:
    root1.append(elem)

tree1.write('epg.xml')
