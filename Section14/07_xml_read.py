import xml.etree.ElementTree as ET

file = open('dataset.xml','rt')
data = file.read()
# print(data)
xml_parse = ET.fromstring(data)
tree = xml_parse.iter(tag='record')
for d in tree:
    print(d.find('id').text,d.find('first_name').text,d.find('last_name').text,d.find('email').text)
file.close()