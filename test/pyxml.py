import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()

for e in root:
	print e.lineNum, e.tag, e.attrib
