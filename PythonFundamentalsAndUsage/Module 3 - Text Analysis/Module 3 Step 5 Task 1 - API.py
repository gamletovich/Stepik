"""

"""

import requests
import json

with open("D:\\Downloads\\dataset_24476_3.txt") as file:
    for number in file:
        number = number.strip()
        url = 'http://numbersapi.com/{}/math?json=true'.format(number)
        res = requests.get(url).text
        data = json.loads(res)
        if data['found']:
            print('Interesting')
        else:
            print('Boring')
