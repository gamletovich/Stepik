# Vasya was appointed the manager of the tourist group and he approached the preparation responsibly,
# compiling a food guide indicating the calorie content per 100 grams, as well as the protein content,
# fat and carbohydrates per 100 grams of product. He couldn't find all the information
# so some cells were left blank (you can consider their value equal to zero).
# He also used some strange office suite and separated the integer and fractional parts with a comma.
# The table is available at https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx
#
# Vasya wants to minimize the weight of food and for this to take the most high-calorie foods.
# Help him and arrange foods in descending order of calories.
# In case the products have the same calorie content, sort them by name.
# Submit the product names as an answer, one per line.
""""""
# Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно,
# составив справочник продуктов с указанием калорийности на 100 грамм, а также содержание белков,
# жиров и углеводов на 100 грамм продукта. Ему не удалось найти всю информацию,
# поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю).
# Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой.
# Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx
#
# Вася хочет минимизировать вес продуктов и для этого брать самые калорийные продукты.
# Помогите ему и упорядочите продукты по убыванию калорийности.
# В случае, если продукты имеют одинаковую калорийность - упорядочите их по названию.
# В качестве ответа необходимо сдать названия продуктов, по одному в строке.

import pandas as pd

data = pd.ExcelFile('D:\\Downloads\\trekking1.xlsx').parse()
print(*data.sort_values(by=['ККал на 100', 'Unnamed: 0'], ascending=[False, True])["Unnamed: 0"].to_list(), sep='\n')


