"""
Your program will have access to the foo function, which can throw exceptions.

You need to write code that runs this function, then catches the ArithmeticError, AssertionError, ZeroDivisionError exceptions, and outputs the name of the caught exception.

Example of a solution that you should submit for review.

try:
foo()
except Exception:
print("Exception")
except BaseException:
print("BaseException")
Hint: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""

"""
Вашей программе будет доступна функция foo, которая может бросать исключения.

Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.

Пример решения, которое вы должны отправить на проверку.

try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
Подсказка: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""

try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError ")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")
