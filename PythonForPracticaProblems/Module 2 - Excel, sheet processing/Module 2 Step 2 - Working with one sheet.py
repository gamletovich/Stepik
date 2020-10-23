# Vasya is planning a career and moving.
# For this, I made a table in which I wrote down salaries for each region for different professions of interest to it.
# The table is available at https://stepik.org/media/attachments/lesson/245267/salaries.xlsx.
# Print the name of the region with the highest median salary
# (the median is the element in the middle of the array after it has been ordered)
# and, separated by a space, the name of the profession with the highest average salary in all regions.

# Вася планирует карьеру и переезд.
# Для это составил таблицу, в которой для каждого региона записал зарплаты для разных интересные ему профессий.
# Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245267/salaries.xlsx.
# Выведите название региона с самой высокой медианной зарплатой
# (медианой называется элемент, стоящий в середине массива после его упорядочивания)
# и, через пробел, название профессии с самой высокой средней зарплатой по всем регионам.

import xlrd
from numpy import median, mean

wb = xlrd.open_workbook('D:\\Downloads\\salaries.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])

cities = sh.col_values(0, 1)
jobs = sh.row_values(0, 1)

salaries_job = {}
salaries_city = {}

for job in jobs:
    salaries_job[job] = sh.col_values(jobs.index(job) + 1, 1)

mean_salary_job = []
for _ in salaries_job:
    mean_salary_job.append(mean(salaries_job[_]))
max_mean_value_job = jobs[mean_salary_job.index(max(mean_salary_job))]

for city in cities:
    salaries_city[city] = sh.row_values(cities.index(city) + 1, 1)

median_value_per_city = []
for key in salaries_city:
    median_value_per_city.append(median(sorted(salaries_city[key])))

max_median_value_city = cities[median_value_per_city.index(max(median_value_per_city))]

print(max_median_value_city, max_mean_value_job)


'''----------using pandas----------'''
import pandas as pd

data = pd.read_excel('D:\\Downloads\\salaries.xlsx', index_col=0)
print(data.median(axis=1).idxmax(), data.mean(axis=0).idxmax())

