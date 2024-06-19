'''в) Запишите каждый из этих словарей в отдельный json-файл.'''

import json
with open('fcc.json', 'rt') as fcc_file:
    fcc_data = json.load(fcc_file)

i = 1
for key,val in fcc_data.items():
    result = dict()
    result[key] = [val]
    print(result)

    filename = f"{i}.json"
    with open(filename, 'wt') as fcc_file:
        json.dump(result, fcc_file)
    i += 1








