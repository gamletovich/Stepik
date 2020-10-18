# There is one table in the file https://stepik.org/media/attachments/lesson/209723/5.html.
# Sum all the numbers in it. Now we have not only added different tags to change the display style,
# but also rendered invalid HTML (although browsers render it, but BeautifulSoup may have problems).
# Invalid HTML code is not uncommon on the Internet, you need to learn to work with this too.
#
# You can fix the html code or try using a non-standard html parser like html5lib.

# В файле https://stepik.org/media/attachments/lesson/209723/5.html находится одна таблица.
# Просуммируйте все числа в ней. Теперь мы не только добавили разных тегов для изменения стиля отображения,
# но и сделали невалидный HTML-код (правда, браузеры его отображают, а вот с BeautifulSoup могут быть проблемы).
# Невалидный HTML-код - не редкость в интернете, надо учиться работать и с этим.
#
# Вы можете исправить html-код или попробовать использовать нестандартный парсер html, такой как html5lib.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


resp = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html')  # downloading file / скачиваем файл
html = resp.read().decode('utf8')  # read the input / считываем содержимое
soup = BeautifulSoup(html, 'html.parser')  # making a soup / делаем суп

table = soup.find('table', attrs={'class': 'wikitable sortable'})

sum = 0
for tag in soup.find_all('td'):
    sum += int(tag.string)
print(sum)