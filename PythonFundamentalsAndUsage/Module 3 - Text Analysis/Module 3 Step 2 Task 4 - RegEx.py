"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
Sample Input:

\w denotes word character
No slashes here
Sample Output:

\w denotes word character
"""
import re
import sys
pattern = r'\b(.+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)