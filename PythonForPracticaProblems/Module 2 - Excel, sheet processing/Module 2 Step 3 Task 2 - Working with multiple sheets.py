# Vasya was appointed the manager of the tourist group and he approached the preparation responsibly,
# compiling a food guide indicating the calorie content per 100 grams, as well as the protein content,
# fat and carbohydrates per 100 grams of product. He couldn't find all the information
# so some cells were left blank (you can consider their value equal to zero).
# He also used some strange office suite and separated the integer and fractional parts with a comma.
# The table is available at https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx
#
# Vasya made a layout for products for one day (it is on the "Layout" sheet)
# indicating the name of the product and its quantity in grams.
# Count 4 numbers: total calories and grams of proteins, fats and carbohydrates.
# Round the numbers down to integers and enter them separated by a space.
""""""
# Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно,
# составив справочник продуктов с указанием калорийности на 100 грамм, а также содержание белков,
# жиров и углеводов на 100 грамм продукта. Ему не удалось найти всю информацию,
# поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю).
# Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой.
# Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx
#
# Вася составил раскладку по продуктам на один день (она на листе "Раскладка")
# с указанием названия продукта и его количества в граммах.
# Посчитайте 4 числа: суммарную калорийность и граммы белков,жиров и углеводов.
# Числа округлите до целых вниз и введите через пробел.

import pandas as pd
import math

data = pd.ExcelFile('D:\\Downloads\\trekking2.xlsx')

sheet_1 = data.parse(data.sheet_names[0])
sheet_2 = data.parse(data.sheet_names[1])

dict_items = sheet_1.sort_values(by=['Unnamed: 0'])["Unnamed: 0"].to_list()
dict_calorie_content = sheet_1.sort_values(by=['Unnamed: 0'])['ККал на 100'].to_list()
dict_protein_content = sheet_1.sort_values(by=['Unnamed: 0'])['Б на 100'].to_list()
dict_fat_content = sheet_1.sort_values(by=['Unnamed: 0'])['Ж на 100'].to_list()
dict_carbohydrates_content = sheet_1.sort_values(by=['Unnamed: 0'])['У на 100'].to_list()

plan_items = sheet_2.sort_values(by=['Продукт'])["Продукт"].to_list()
plan_amount = sheet_2.sort_values(by=['Продукт'])['Вес в граммах'].to_list()

sum_calorie = 0
sum_protein = 0
sum_fat = 0
sum_carbohydrates = 0

for el in plan_items:

    amount = plan_amount[plan_items.index(el)]
    calorie = dict_calorie_content[dict_items.index(el)]
    protein = dict_protein_content[dict_items.index(el)]
    fat = dict_fat_content[dict_items.index(el)]
    carbohydrates = dict_carbohydrates_content[dict_items.index(el)]

    print("{:<35} {:<5} {:<7} {:<5} {:<5} {:<5}".format(el, amount, calorie, protein, fat, carbohydrates),
          end="   ---   ")

    sum_calorie = sum_calorie + (amount / 100 * calorie)
    sum_protein = sum_protein + (amount / 100 * protein)
    sum_fat = sum_fat + (amount / 100 * fat)
    if dict_carbohydrates_content[dict_items.index(el)] > 0:
        sum_carbohydrates = sum_carbohydrates + (amount / 100 * carbohydrates)

    print(math.trunc(sum_calorie), end=" ")
    print(math.trunc(sum_protein), end=" ")
    print(math.trunc(sum_fat), end=" ")
    print(math.trunc(sum_carbohydrates))

print(math.trunc(sum_calorie), end=" ")
print(math.trunc(sum_protein), end=" ")
print(math.trunc(sum_fat), end=" ")
print(math.trunc(sum_carbohydrates))
