"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
"""
import json

"""преобразуем изначальную структуру данных, создаём словарь c элементами "дитя:[родители]"""""
cls = {c['name']: c['parents'] for c in json.loads(input())}
"""
создаём ссылку на рекурсивную функцию, записанную с помощью lambda-конструктора
функция возвращает True, если имена class_name1 и class_name2 совпадают
иначе она вызывает саму себя, при этом в качестве параметра class_name2
передаётся по очереди каждый родитель класса "class_name2" из текущего вызова,
а параметр class_name1 всегда остаётся тем же, что и при первом вызове
"""
isbase = lambda class_name1, class_name2: (
        class_name1 == class_name2 or any(isbase(class_name1, i) for i in cls[class_name2]))

"""
def isbase(class_name1, class_name2):
    if class_name1 == class_name2:
        return True
    else:
        for i in cls[class_name2]:
            if isbase(class_name1, i):
                return True
        return False
"""
"""
для каждого ключа, описанного в словаре
находим длину от множества, в которое добавляем имя каждого класса - class_name2,
если рекурсивная функция isbase(class_name1, class_name2) возвращает True
"""
for class_name1 in sorted(cls):
    print(class_name1, ':', len({class_name2 for class_name2 in cls if isbase(class_name1, class_name2)}))
