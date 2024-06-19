'''а) Прочитайте из трёх excel файлов (заранее создайте их, внутри 1111, 2222, 3333)'''
import json
fcc = {"userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False}
with open('fcc.json', 'wt')as file1:
    json.dump(fcc,file1)
