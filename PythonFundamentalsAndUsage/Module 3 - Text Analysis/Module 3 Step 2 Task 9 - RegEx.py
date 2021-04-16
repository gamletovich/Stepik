"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:

attraction
buzzzz
Sample Output:

atraction
buz
"""
import re
import sys

pattern = r'(\w)\1+'

for line in sys.stdin:
    print(re.sub(pattern, r'\2\1\3', line.rstrip()))