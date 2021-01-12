"""
Write an implementation of the closest_mod_5 function that takes an integer as a single argument and returns x
the smallest integer r, what is :

y is greater than or equal to X
Y 5 5
Format of what is expected of you as a response:

def closest_mod_5( x):
if x % 5 == 0:
return x
return "I do not know :("
"""

"""
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую
самое маленькое целое число y, такое что:

y больше или равно x
y делится нацело на 5
Формат того, что ожидается от вас в качестве ответа:

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return "I don't know :("
"""


def closest_mod_5(x):
    y = (x + 4) // 5

    return y * 5
