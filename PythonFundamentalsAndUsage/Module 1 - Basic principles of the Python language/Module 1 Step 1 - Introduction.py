"""
If the following task seems difficult to you, then you should take the first course in Python, which does not require
initial knowledge of the language: https://stepic.org/course/Programming-in-Python-67.

Implement a program that takes a sequence of numbers and outputs their sum.

Your program is fed a sequence of strings as input.
The first line contains the number n (1 ≤ n ≤ 100).
The next n lines contain one integer each.

Print one number-the sum of the given n numbers.

Note:
To read a single number from a standard input stream, you can use, for example, the following code

n = int(input())
"""

"""
Если приведенная ниже задача кажется вам сложной, то вам следует пройти первый курс по языку Python, который не 
требует начальных знаний языка: https://stepic.org/course/Программирование-на-Python-67﻿.

Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.

Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.

Выведите одно число – сумму данных n чисел.

Примечание:
﻿Чтобы считать одно число из стандартного потока ввода, можно использовать, например, следующий код

n = int(input())
"""

i = int(input())
s = 0

while i != 0:
    s = s + int(input())
    i = i - 1

print(s)
