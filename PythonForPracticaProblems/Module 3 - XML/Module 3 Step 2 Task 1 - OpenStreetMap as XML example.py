"""
In this task, you just need to install the xmltodict library,
download the file https://stepik.org/media/attachments/lesson/245571/map1.osm,
create a script in the directory with the file with the following content:

import xmltodict

fin = open ('map1.osm', 'r', encoding = 'utf8')
xml = fin.read ()
fin.close ()

parsedxml = xmltodict.parse (xml)
print (parsedxml ['osm'] ['node'] [100] ['@ id'])
and will provide the output of this script as a response.
"""
"""
В этой задаче нужно просто установить библиотеку xmltodict,
скачать файл https://stepik.org/media/attachments/lesson/245571/map1.osm,
создать в директории с файлом скрипт со следующим содержанием:

import xmltodict

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])
и ввести в качестве ответа вывод этого скрипта.
"""

import xmltodict

fin = open('D:\\Downloads\\map1.osm', 'r', encoding='utf8')

text = fin.read()

fin.close()
dct = xmltodict.parse(text)
count_in= 0
count_without = 0
for node in dct['osm']['node']:
    if 'tag' in node:
        count_in += 1
    else:
        count_without += 1
print(count_in, count_without)



