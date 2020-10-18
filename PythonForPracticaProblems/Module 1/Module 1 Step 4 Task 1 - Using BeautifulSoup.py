# There is one table in the file https://stepik.org/media/attachments/lesson/209723/3.html.
# Sum all the numbers in it and enter one number as an answer - this amount.
# Use BeautifulSoup to access cells.

# В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица.
# Просуммируйте все числа в ней и введите в качестве ответа одно число - эту сумму.
# Для доступа к ячейкам используйте возможности BeautifulSoup.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html')  # downloading file / скачиваем файл
html = resp.read().decode('utf8')  # read the input / считываем содержимое
soup = BeautifulSoup(html, 'html.parser')  # making a soup / делаем суп

table = soup.find('table', attrs={'class': 'wikitable sortable'})
sum = 0
for tag in soup.find_all('td'):
    sum += int(tag.string)
print(sum)