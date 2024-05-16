import json
import pathlib
import os

base_dir = pathlib.Path(__file__).resolve().parent
path = os.path.join(base_dir, 'data', 'people.json')

file = open(path, encoding='utf-8')
people = json.load(file)
file.close()  # exit

print(people['1'][-1]['remote'])
