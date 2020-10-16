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
