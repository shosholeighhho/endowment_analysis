import os
import xml.etree.ElementTree as ET



def get_value(el):
	return el.text if el is not None else None



ele_names = set()
num_files_explored = 0


for filename in os.listdir("../data"):
	num_files_explored += 1
	if num_files_explored > 100:
		print(ele_names)
		print('==============================================')
	#tree = ET.parse("../data/file_201840689349300619.xml")
	tree = ET.parse(f'../data/{filename}')
	root = tree.getroot()

	data = root.findall('.//{http://www.irs.gov/efile}ReturnData')
	if not data:
		continue



	scheduled = data[0].findall('.//{http://www.irs.gov/efile}IRS990ScheduleD')
	if not scheduled:
		continue

	for element in scheduled[0]:
	    ele_name = element.tag.split('}')[1]
	    ele_names.add(ele_name)
	    #ele_value = scheduled[ 0].find(element.tag).text
	    #print(ele_name, ' : ', ele_value)