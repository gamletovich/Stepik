"""
In this task, you need to learn how to generate html code in Python and submit an html file for review,
in which there will be a 10 by 10 table, which should contain a multiplication table for numbers from 1 to 10.
When you open your file in a browser, it should look something like this:

Your file must start with <html> and <body> tags and end with </body> and </html>.

To create a table, you can use the <table> tags (create a table),
<tr> (create a row in the table) and <td> (create a separate cell).
All open tags must be closed, and this must be done in the correct order.

Please do not use any decorations or other tags - we will not be able to test such solutions
"""
"""
В этой задаче вам необходимо научиться генерировать html-код на питоне и сдать на проверку html-файл,
в котором будет таблица размером 10 на 10, которая должна содержать таблицу умножения для чисел от 1 до 10.
При открытии вашего файла в браузере это должно выглядеть примерно так:

Ваш файл должен начинаться с тегов <html> и <body> и заканчиваться </body> и </html>.

Для создания таблицы можно пользоваться тегами <table> (создание таблицы),
<tr> (создание строки в таблице) и <td> (создание отдельной ячейки).
Все открытые теги нужно закрыть, причем сделать это нужно в правильном порядке.

Пожалуйста, не используйте никаких украшений и других тегов - мы не сможем проверить такие решения
"""

from prettytable import PrettyTable


def mult_table():
    table = PrettyTable()
    for row in range(1, 11):
        temp = []
        for column in range(1, 11):
            temp.append(row * column)
        table.add_row(temp)
        table.header = False
    print(table.get_html_string())


mult_table()
