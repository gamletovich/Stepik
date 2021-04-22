"""
In order for us to present data beautifully, we need to learn how to create html files manually.
We have already analyzed them and have some idea about their structure, but, as usual,
you can find the information you need to create html files in a search engine.

In this task, you need to submit an html file for review, which will contain a 2 by 2 table,
which should contain numbers 1 and 2 in the cells of the first row, and numbers 3 and 4 in the cells of the second row.
When you open your file in a browser, it should look something like this:



Your file must start with <html> and <body> tags and end with </body> and </html>.

To create a table, you can use the <table> tags (create a table),
<tr> (create a row in the table) and <td> (create a separate cell).
All open tags must be closed, and this must be done in the correct order.

Please do not use any decorations or other tags - we will not be able to test such solutions.
"""
"""
Чтобы мы могли представлять данные красиво, необходимо научиться создавать html-файлы вручную.
Мы уже анализировали их и имеем некоторое представление об их устройстве, но, как обычно,
можно найти необходимую для создания html-файлов информацию в поисковике.

В этой задаче вам необходимо сдать на проверку html-файл, в котором будет таблица размером 2 на 2,
которая должна содержать в ячейках первой строки числа 1 и 2, а в ячейках второй строки числа 3 и 4.
При открытии вашего файла в браузере это должно выглядеть примерно так:



Ваш файл должен начинаться с тегов <html> и <body> и заканчиваться </body> и </html>.

Для создания таблицы можно пользоваться тегами <table> (создание таблицы),
<tr> (создание строки в таблице) и <td> (создание отдельной ячейки).
Все открытые теги нужно закрыть, причем сделать это нужно в правильном порядке.

Пожалуйста, не используйте никаких украшений и других тегов - мы не сможем проверить такие решения.
"""
from prettytable import PrettyTable

pt = PrettyTable()
pt.add_column("", [1, 3])
pt.add_column("", [2, 4])
print(str(pt.get_html_string()))
# print(pt.get_string())
