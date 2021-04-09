"""
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.
Пример архива
Пример ответа
"""
import os

os.chdir(r"D:\Downloads")
directories = []
for current_dir, dirs, files in os.walk("main"):
    for file in files:
        if file[-3:] == ".py" \
                and current_dir not in directories:
            directories.append(current_dir)

with open("D:\\Downloads\\result.txt", "w") as r:
    for el in sorted(directories):
        r.write(el + "\n")
