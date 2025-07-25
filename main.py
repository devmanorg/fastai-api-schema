import json
from pprint import pprint

with open('openapi.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Красиво выводим содержимое
pprint(data)
