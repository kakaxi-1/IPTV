import xml.etree.ElementTree as ET

def merge_xml_files(output_file, *input_files):

    root = ET.Element("root")
    
    for xml_file in input_files:

        tree = ET.parse(xml_file)

        xml_root = tree.getroot()

        root.extend(xml_root)
    
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

merge_xml_files("epg.xml", "e.xml", "epg_part.xml")
