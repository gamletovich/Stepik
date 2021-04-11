"""

"""
import csv
from collections import Counter as c

with open("D:\\Downloads\\Crimes.csv") as f:
    data = csv.reader(f)
    print(c(row[5] for row in data if '2015' in row[2]))