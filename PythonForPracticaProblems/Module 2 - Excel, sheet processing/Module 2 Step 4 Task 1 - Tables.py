"""
The chief accountant of Horns and Hoofs accidentally deleted the payroll.
Fortunately, he has the pay slips of all the employees.
Help with these pay slips to restore the payroll.
Archive with pay slips is available here
https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip
(you can download and unpack it manually or learn how to do it yourself using a Python script).

The statement must contain 1000 lines, each line must contain the full name of the employee and, separated by a space, his salary.
Employees should be sorted alphabetically.
"""
"""
Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой.
К счастью, у него сохранились расчётные листки всех сотрудников.
Помогите по этим расчётным листкам восстановить зарплатную ведомость.
Архив с расчётными листками доступен по ссылке
https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip
(вы можете скачать и распаковать его вручную или самостоятельно научиться делать это с помощью скрипта на Питоне).

Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел, его зарплата.
Сотрудники должны быть упорядочены по алфавиту.
"""
import requests
from zipfile import ZipFile
from io import BytesIO
import pandas as pd

url = "https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip"
r = requests.get(url)
z = ZipFile(BytesIO(r.content))
z.extractall("D:\\Downloads\\rogaikopyta")

file_names = z.namelist()
result = pd.DataFrame(columns=["ФИО", "Начислено"])

for name in file_names:
    i = file_names.index(name)
    file_name = "D:\\Downloads\\rogaikopyta\\" + name
    file = pd.ExcelFile(file_name).parse()
    result.at[i, 'ФИО'] = file['Unnamed: 1'].values[0]
    result.at[i, 'Начислено'] = str(file['Unnamed: 3'].values[0])[:-2]

result = result.sort_values("ФИО")
result.to_csv("D:\\Downloads\\result.csv",
              encoding='utf-8-sig',
              sep=" ",
              header=False,
              index=False,
              quoting=None)

