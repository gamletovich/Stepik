"""
Implement a program that will emulate working with namespaces. You need to implement support for creating namespaces
and adding variables to them.

In this task, each namespace has a unique text identifier – its name.

Your program receives the following input requests:

create <namespace> <parent> - create a new namespace with the name <namespace> inside the <parent>space
add <namespace> <var> – add the <var>variable to the <namespace> space
get <namespace> <var> - get the name of the space from which the <var > variable will be taken when querying from the <namespace> space, or None if such a space does not exist
Consider a set of queries

add global a
create foo global
add foo b
create bar foo
add bar a
The namespace structure described by these queries will be equivalent to the namespace structure created when running this code

a = 0
def foo():
b = 1
def bar():
a = 2
In the main body of the program, we declare the variable a, thereby adding it to the global space. Next, we declare the function foo, which entails creating a local namespace for it inside the global space. In our case, this is described by the create foo global command. Next, we declare the function bar inside the function foo, thereby creating a space bar inside the space foo, and add the variable a to bar.

Adding get requests to our requests

get foo a
get foo c
get bar a
get bar b
Let's imagine what this might look like in the code

a = 0
def foo():
b = 1
get(a)
get(c)
def bar():
a = 2
get(a)
get (b)
The result of the get request will be the name of the space from which the desired variable will be taken.
For example, the result of the get foo a request will be global, because the variable a is not declared in the foo space, but in the global space inside which the foo space is located, it is declared. Similarly, the result of the get bar b request will be foo, and the result of get bar a will be bar.

The result of get foo c will be None, because neither the foo space nor its outer global space has been declared variable C.

More formally, the result of get <namespace> <var> is

<namespace>, if the <var> variable was declared in the <namespace>space
get <parent> <var> - result of a request to the space inside which the <namespace> space was created, if the variable was not declared
None if <parent> does not exist, i.e. <namespace> is global
The format of the input data
The first line contains the number n (1 ≤ n ≤ 100) – the number of requests.
Each of the following n lines contains one query.
Queries are executed in the order in which they are given in the input data.
Namespace names and variable names are strings of length no more than 10, consisting of lowercase Latin letters.

Output format
For each get request, print its result in a separate line.



Sample Input:

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
Sample Output:

global
None
bar
foo
"""

"""
Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует
Рассмотрим набор запросов

add global a
create foo global
add foo b
create bar foo
add bar a
Структура пространств имен описанная данными запросами будет эквивалентна структуре пространств имен, созданной при выполнении данного кода

a = 0
def foo():
  b = 1
  def bar():
    a = 2
В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство global. Далее мы объявляем функцию foo, что влечет за собой создание локального для нее пространства имен внутри пространства global. В нашем случае, это описывается командой create foo global. Далее мы объявляем внутри функции foo функцию bar, тем самым создавая пространство bar внутри пространства foo, и добавляем в bar переменную a.

Добавим запросы get к нашим запросам

get foo a
get foo c
get bar a
get bar b
Представим как это могло бы выглядеть в коде

a = 0
def foo():
  b = 1
  get(a)
  get(c)
  def bar():
    a = 2
    get(a)
    get(b)
Результатом запроса get будет имя пространства, из которого будет взята нужная переменная.
Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена переменная a, но в пространстве global, внутри которого находится пространство foo, она объявлена. Аналогично, результатом запроса get bar b будет являться foo, а результатом работы get bar a будет являться bar.

Результатом get foo c будет являться None, потому что ни в пространстве foo, ни в его внешнем пространстве global не была объявлена переменная с.

Более формально, результатом работы get <namespace> <var> является

<namespace>, если в пространстве <namespace> была объявлена переменная <var>
get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>, если переменная не была объявлена
None, если не существует <parent>, т. е. <namespace>﻿ – это global
Формат входных данных
В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
В каждой из следующих n строк дано по одному запросу.
Запросы выполняются в порядке, в котором они даны во входных данных.
Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных латинских букв.

Формат выходных данных
Для каждого запроса get выведите в отдельной строке его результат.



Sample Input:

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
Sample Output:

global
None
bar
foo
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
