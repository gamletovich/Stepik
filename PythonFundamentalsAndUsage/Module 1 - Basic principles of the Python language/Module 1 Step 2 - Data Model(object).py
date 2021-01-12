"""Implement a program that will calculate the number of different objects in the list.
Two objects a and and are considered distinct if a is and is False.

Your program has access to a variable called objects, which refers to a list containing no more than 100 objects.
Print the number of different objects in this list.

The format of the expected program:

ans = 0
for obj in objects: # available variable objects
ans += 1

print(ans)

Note:
The number of distinct objects is the maximum size of a set of objects in which any two objects are distinct.

Consider an example:
objects = [1, 2, 1, 2, 3] # we will assume that the same numbers correspond to the same objects,
and different ones – to different ones

Then all the different objects are the set {1, 2, 3}. Thus, the number of different objects is three."""

"""
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
Два объекта a и b считаются различными, если a is b равно False.

Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов. 
Выведите количество различных объектов в этом списке.

Формат ожидаемой программы:

ans = 0
for obj in objects: # доступная переменная objects
    ans += 1

print(ans)

Примечание:
Количеством различных объектов называется максимальный размер множества объектов, 
в котором любые два объекта являются различными.

Рассмотрим пример:
objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам, 
а различные – различным

Тогда все различные объекты являют собой множество {1, 2, 3}﻿. 
Таким образом, количество различных объектов равно трём.
"""

checker = set()

ans = 0

for obj in objects:
    if id(obj) not in checker:
        checker.add(id(obj))

print(len(checker))
