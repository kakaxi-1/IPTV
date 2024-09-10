import xml.etree.ElementTree as ET

def merge_xml_files(files):
    try:
        root = None
        for file in files:

            with open(file, 'r', encoding='utf-8') as f:
                tree = ET.parse(f)
                if root is None:
                    root = tree.getroot()
                else:
                    root.extend(tree.getroot())


        tree = ET.ElementTree(root)
        with open('epg.xml', 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
            
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


merge_xml_files(["e.xml", "epg_part.xml"])
