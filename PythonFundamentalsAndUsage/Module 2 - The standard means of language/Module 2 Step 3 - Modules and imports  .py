"""
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное
целое число бросалось исключение NonPositiveError и число не добавлялось, а при попытке добавить положительное целое
число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.

Примечание:
Положительными считаются числа, строго большие нуля.
"""

class NonPositiveError(BaseException):
    pass

class PositiveList(list):
    def append(self, item):
        if item > 0:
            super(PositiveList, self).append(item)  # append the item to itself (the list)
        else:
            raise NonPositiveError
