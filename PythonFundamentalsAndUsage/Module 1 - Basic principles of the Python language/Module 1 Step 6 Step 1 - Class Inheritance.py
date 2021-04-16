"""
You are given a description of class inheritance in the following format.
<class name 1> : <class name 2> <class name 3> ... <class name k>
This means that class 1 is inherited from class 2, class 3, etc.

Or equivalent to writing:

class Class1(Class2, Class3 ... ClassK):
pass
Class A is a direct ancestor of class B if B is inherited from A:


class B(A):
pass


Class A is an ancestor of class B if
A = B;
A is the direct ancestor of B
there is a class C such that C is the direct ancestor of B and A is the ancestor of C

For example:
class B(A):
pass

class C(B):
pass

# A -- ancestor With


You need to answer queries whether one class is an ancestor of another class

Important Note:
You do not need to create classes.
We ask you to model this process and see if there is a path from one class to another.
The format of the input data
The first line of input contains an integer n - the number of classes.

The next n lines contain a description of class inheritance. The i-th line indicates which classes the i-th class inherits from. Note that the class may not be inherited from anyone. It is guaranteed that the class is not inherited from itself (directly or indirectly), that the class is not inherited explicitly from the same class more than once.

The next line contains the number q - the number of requests.

The following q lines contain a description of the queries in the format <class name 1> <class name 2>.
Class name – a string consisting of Latin characters, no longer than 50.

Output format
For each query, print in a separate line the word "Yes" if Class 1 is an ancestor of class 2, and "No" if it is not.
"""

"""
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.
"""

number_of_classes = int(input())

classes = {}

for i in range(number_of_classes):
    line = input().split(":")

    if len(line) != 1:
        key, values = line[0].replace(' ', ''), (line[1].split(" ")[1:])
        classes[key] = values
    else:
        key, values = line[0], ""
        classes[key] = values

number_of_request = int(input())
requests = []

for i in range(number_of_request):
    requests.append((input().split(" ")))


def check_classes(dictionary, parent, child):
    temp = dictionary[child].count(parent)

    if parent in dictionary[child]:
        return "Yes"
    elif parent == child:
        return "Yes"
    elif dictionary[child] == '':
        return "No"
    else:
        result = "No"
        for elements in dictionary[child]:
            if check_classes(dictionary, parent, elements) == "Yes":
                result = "Yes"
                break
        return result


for req in requests:
    print(check_classes(classes, req[0], req[1]))
"""
10
classA : classB classC classD classG classH
classB : classC classE classG classH classK classL
classC : classE classD classH classK classL
classE : classD classF classK classL
classD : classG classH
classF : classK
classG : classF
classH : classL
classK : classH classL
classL
38
classK classD Yes
classD classA Yes
classG classD Yes
classH classA Yes
classE classE Yes
classH classG Yes
classE classL No
classB classD No
classD classL No
classD classG No
classD classE Yes
classA classF No
classA classC No
classK classA Yes
classA classH No
classK classD Yes
classH classB Yes
classK classB Yes
classD classL No
classG classG Yes
classA classH No
classK classL No
classG classE Yes
classB classA Yes
classC classK No
classK classL No
classC classL No
classG classC Yes
classD classD Yes
classC classG No
classE classA Yes
classF classK No
classB classG No
classH classL No
classL classF Yes
classH classG Yes
classD classA Yes
classH classL No








10
classA : classB classC classD classG classH
classB : classC classE classG classH classK classL
classC : classE classD classH classK classL
classE : classD classF classK classL
classD : classG classH
classF : classK
classG : classF
classH : classL
classK : classH classL
classL
10
classB classD No
classD classG No
classA classF No
classA classC No
classA classH No
classA classH No
classC classK No
classC classG No
classF classK No
classB classG No


11
A,
B : A
C : A
D : B C
E : D
F : D
X
Y : X A
Z : X
V : Z Y
W : V
8
A G Yes
A Z No
A W Yes
X W Yes
X QWE  No
A X No
X X Yes
1 1 No
"""
