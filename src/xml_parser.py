import xml.etree.ElementTree as ET


tree = ET.parse("../file_201840689349300619.xml")
root = tree.getroot()

def get_value(el):
	return el.text if el is not None else None


data = root.findall('.//{http://www.irs.gov/efile}ReturnData')[0]

scheduled = data.findall('.//{http://www.irs.gov/efile}IRS990ScheduleD')

print(scheduled)

for child in scheduled:
	print(child.tag, child.attrib)
