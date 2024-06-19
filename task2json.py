'''б) Прочитайте этот файл в массив python-словарей.'''
import json
with open('fcc.json', 'rt') as fcc_file:
    fcc_data = json.load(fcc_file)
    print(fcc_data)