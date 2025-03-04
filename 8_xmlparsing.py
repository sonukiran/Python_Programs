import xml.etree.ElementTree as ET
xml_data = """<person>
    <name>Alice</name>
    <age>25</age>
    <city>New York</city>
</person>"""
root = ET.fromstring(xml_data)
print(root.findtext("name"))