# The file https://stepik.org/media/attachments/lesson/209719/2.html contains a Wikipedia article on Python.
# This article contains code tags that distinguish Python constructs.
# You need to find all the lines between the <code> and </code> tags and find those lines
# which occur most often and print them in alphabetical order, separated by spaces.
#
# For example, if the original text of the page would look like this:
#
# <code> a </code>
# <a> bracadabr </a>
# <code> c </code>
# <code> b </code>
# <code> b </code>
# <code> c </code>
# then the answer would be "b c".

# Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python.
# В этой статье есть теги code, которыми выделяются конструкции на языке Python.
# Вам нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки,
# которые встречаются чаще всего и вывести их в алфавитном порядке, разделяя пробелами.
#
# Например, если исходный текст страницы выглядел бы так:
#
# <code>a</code>
# <a>bracadabr</a>
# <code>c</code>
# <code>b</code>
# <code>b</code>
# <code>c</code>
# то в ответ надо было бы ввести строку "b c".

from urllib.request import urlopen
import re
import collections

html = urlopen(" https://stepik.org/media/attachments/lesson/209719/2.html").read().decode("utf-8")
s = str(html)

regex = '<code>(.*?)</code>'

l = sorted(re.findall(regex, s))
counter = collections.Counter(l)

max_counter = max(counter.values())

answer = ""

for k, v in counter.items():
    if v == max_counter:
        print(k, v)
        answer = answer + k + " "

print(answer)
