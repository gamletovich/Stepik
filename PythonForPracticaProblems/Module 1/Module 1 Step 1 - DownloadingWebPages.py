# We saved the Wikipedia page about programming languages
# and saved it at https://stepik.org/media/attachments/lesson/209717/1.html
#
# Download it using a Python script and calculate which language is mentioned more often Python or C ++
# (the answer must be one of these two lines).

# Мы сохранили страницу с википедии про языки программирования
# и сохранили по адресу https://stepik.org/media/attachments/lesson/209717/1.html
#
# Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще Python или C++
# (ответ должен быть одной из этих двух строк).

from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode("utf-8")

if str(html).count("C++") > str(html).count("Python"):
    print("C++: ", str(html).count("C++"))
else:
    print("Python: ", str(html).count("Python"))