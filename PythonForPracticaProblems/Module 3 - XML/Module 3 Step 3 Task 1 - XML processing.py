"""
Vasya decided to open a petrol station (gas station).
To assess the level of competition, he wants to study the number of gas stations in the area of interest to him.
Vasya downloaded the OSM map piece he was interested in https://stepik.org/media/attachments/lesson/245681/map2.osm
and wants to calculate how many point objects (node) are marked on it, which are a gas station.
As an answer, you need to output one number - the number of gas stations.

"How refueling is indicated in OpenStreetMap" -
an example of a good query to see how refueling is indicated in OpenStreetMap.
"""
"""
Вася решил открыть АЗС (заправку).
Чтобы оценить уровень конкуренции он хочет изучить количество заправок в интересующем его районе.
Вася скачал интересующий его кусок карты OSM https://stepik.org/media/attachments/lesson/245681/map2.osm
и хочет посчитать, сколько на нём отмечено точечных объектов (node), являющихся заправкой.
В качестве ответа вам необходимо вывести одно число - количество АЗС.

"Как обозначается заправка в OpenStreetMap" -
пример хорошего запроса чтобы узнать, как обозначается заправка в OpenStreetMap.
"""

import xmltodict

fin = open('D:\\Downloads\\map2.osm', 'r', encoding='utf8')

text = fin.read()

fin.close()
dct = xmltodict.parse(text)
count = 0
for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if (tag['@v']) == 'fuel':
                    count += 1
        elif isinstance(tags, dict):
            if (tags['@v']) == 'fuel':
                count += 1
print(count)
