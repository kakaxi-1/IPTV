import xml.etree.ElementTree as ET

def merge_xml_files(files):
    root_elements = []
    for file in files:
        tree = ET.parse(file)
        root_elements.append(tree.getroot())
    
    merged_root = ET.Element("root")  
    for root in root_elements:
        for child in root:
            merged_root.append(child)
    
    merged_tree = ET.ElementTree(merged_root)
    merged_tree.write("epg.xml", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    merge_xml_files(["e.xml", "epg_part.xml"])
