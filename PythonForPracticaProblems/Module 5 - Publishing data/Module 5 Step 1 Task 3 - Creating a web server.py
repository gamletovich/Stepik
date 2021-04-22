"""
In this task, you will learn how to create links.
You need to generate html-code in python and submit for verification an html-file, which will contain a 10-by-10 table,
which should contain a multiplication table for numbers from 1 to 10. Each number in the table should be a link to a page
http: // <this number> .ru. For example, the number 12 should be a link to the page http://12.ru

When you open your file in a browser, it should look something like this:



Your file must start with <html> and <body> tags and end with </body> and </html>.
To create a table, you can use the <table> tags (create a table),
<tr> (create a row in the table) and <td> (create a separate cell).
All open tags must be closed, and this must be done in the correct order.

Use the <a> tag to create a link. For example, a link to the page http://hse.ru with the text "Higher School of Economics"
should look like this: <a href=http://hse.ru> Higher School of Economics </a>.

Please do not use any decorations or other tags - we will not be able to test such solutions.
"""
"""
В этой задаче вам предстоит научиться создавать ссылки.
Вам нужно сгенерировать html-код на питоне и сдать на проверку html-файл, в котором будет таблица размером 10 на 10,
которая должна содержать таблицу умножения для чисел от 1 до 10. Каждое число в таблице должно быть ссылкой на страницу
http://<это число>.ru. Например, число 12 должно быть ссылкой на страницу http://12.ru

При открытии вашего файла в браузере это должно выглядеть примерно так:



Ваш файл должен начинаться с тегов <html> и <body> и заканчиваться </body> и </html>.
Для создания таблицы можно пользоваться тегами <table> (создание таблицы),
<tr> (создание строки в таблице) и <td> (создание отдельной ячейки).
Все открытые теги нужно закрыть, причем сделать это нужно в правильном порядке.

Для создания ссылки пользуйтесь тегом <a>. Например, ссылка на страницу http://hse.ru с текстом "Высшая школа экономики"
должна выглядеть так: <a href=http://hse.ru>Высшая школа экономики</a>.

Пожалуйста, не используйте никаких украшений и других тегов - мы не сможем проверить такие решения.
"""
from prettytable import PrettyTable


def mult_table(size=10):
    table = PrettyTable()
    for row in range(1, size + 1):
        temp = []
        for column in range(1, size + 1):
            mul = row * column
            href = f"<a href=http://{mul}.ru>{mul}</a>"
            temp.append(href)
        table.add_row(temp)
        table.header = False
    return "<html>\n<body>\n" + \
           table.get_html_string() \
               .replace("&lt;", "<") \
               .replace("&gt;", ">") \
               .replace("\n    <tbody>", "") \
               .replace("\n    </tbody>", "") \
           + "\n</body>\n</html>"


file = open("D:\\Downloads\\result513.txt", "w")
file.write(mult_table())
file.close()
