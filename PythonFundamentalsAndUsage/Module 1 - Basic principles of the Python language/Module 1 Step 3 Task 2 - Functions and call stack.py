"""
A combination of n elements in k is a subset of these n elements of size k.
Two combinations are called different if one of the combinations contains an element that does not contain the other.
The number of combinations from n to k is the number of different combinations from n to k. Let's denote this number as C(n, k).

Example:
Let n = 3, i.e. there are three elements (1, 2, 3). Let k = 2.
All different combinations of 3 elements by 2: (1, 2), (1, 3), (2, 3).
There are three different combinations, so C(3, 2) = 3.

It is easy to understand that C(n, 0) = 1, since there is only one way to choose 0 from n elements, namely, to choose nothing.
It is also easy to understand that if k > n, then C(n, k) = 0, since it is impossible, for example, to choose five elements from three.

To calculate C(n, k) in other cases, the following recurrent formula is used:
C(n, k) = C(n - 1, k) + C(n - 1, k - 1).

Implement a program that computes C(n, k) for the given n and k.

Your program is fed a string containing two integers n and k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
Your program should output a single number: C(n, k).

Note:
You can count two numbers n and k, for example, as follows:

n, k = map(int, input().split())
"""

"""
Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).

Пример:
Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
Различных сочетаний три, поэтому C(3, 2) = 3.

Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего не выбрать.
Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов выбрать пять.

Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
C(n, k) = C(n - 1, k) + C(n - 1, k - 1).

Реализуйте программу, которая для заданных n и k вычисляет C(n, k).

Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
Ваша программа должна вывести единственное число: C(n, k).

Примечание:
Считать два числа n и k вы можете, например, следующим образом:

n, k = map(int, input().split())
"""

n, k = map(int, input().split())


def c(n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    else:
        return c(n - 1, k) + c(n - 1, k - 1)


print(c(n, k))
