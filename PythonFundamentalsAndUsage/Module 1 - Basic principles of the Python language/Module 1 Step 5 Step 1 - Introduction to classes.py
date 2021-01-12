"""
Implement the moneybox class to work with a virtual piggy bank.

Each piggy bank has a limited capacity, which is expressed as an integer – the number of coins that can be put in the
piggy bank. The class should maintain information about the number of coins in the piggy bank, provide the ability to
add coins to the piggy bank, and find out whether it is possible to add some more coins to the piggy bank without
exceeding its capacity.

The class should look like this

class MoneyBox:
def __init__(self, capacity):
# constructor with argument-piggy bank capacity

def can_add(self, v):
# True if you can add v coins, False otherwise

def add(self, v):
# put v coins in the piggy bank
When creating a piggy bank, the number of coins in it is 0.
Note:
It is guaranteed that the add(self, v) method will only be called if can_add(self, v) is True.
"""

"""
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

Класс должен иметь следующий вид

class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        # положить v монет в копилку
При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿.
"""


class MoneyBox:
    def __init__(self, capacity):
        self.max = capacity
        self.amount = 0

    def can_add(self, v):
        if self.amount + v <= self.max:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v) == True:
            self.amount += v
        else:
            print("You rich your maximum")
