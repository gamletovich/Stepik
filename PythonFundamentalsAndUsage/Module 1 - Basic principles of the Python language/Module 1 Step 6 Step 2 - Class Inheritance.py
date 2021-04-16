"""
Implement a data structure that is an extended stack structure. You need to support adding an element to the top of the stack, removing it from the top of the stack, and you need to support addition, subtraction, multiplication, and integer division operations.

The stack addition operation is defined as follows. The top element (top1) is removed from the stack, then the next top element (top2) is removed, and then, as a result of the addition operation, an element equal to top1 + top2 is placed on the top of the stack.

The operations of subtraction (top1 - top2), multiplication (top1 * top2) and integer division (top1 // top2) are defined in the same way.

Implement this data structure as an extendedstack class, inheriting it from the standard list class.
The required class structure:

class extendedstack (list):
def sum(self):
# addition operation

def sub(self):
# the operation of subtraction

def mul(self):
# multiplication operation

def div(self):
# integer division operation

Note
To add an element to the stack, use the append method, and to remove it from the stack, use the pop method.
It is guaranteed that operations will be performed only when there are at least two elements in the stack."""

"""
Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления.

Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент (top1), затем снимается следующий верхний элемент (top2), и затем как результат операции сложения на вершину стека кладется элемент, равный top1 + top2.

Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) и целочисленного деления (top1 // top2).

Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.
Требуемая структура класса:

class ExtendedStack(list):
    def sum(self):
        # операция сложения

    def sub(self):
        # операция вычитания

    def mul(self):
        # операция умножения

    def div(self):
        # операция целочисленного деления
 
Примечание
Для добавления элемента на стек используется метод append, а для снятия со стека – метод pop.
Гарантируется, что операции будут совершаться только когда в стеке есть хотя бы два элемента."""


class ExtendedStack(list):

    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())
