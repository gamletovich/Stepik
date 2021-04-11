"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""
import csv
from collections import Counter as c

with open("D:\\Downloads\\Crimes.csv") as f:
    data = csv.reader(f)
    print(c(row[5] for row in data if '2015' in row[2]))