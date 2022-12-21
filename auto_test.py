import os
import json


w = os.system('python3 -m pycodestyle ./src > /dev/null 2>&1')
s = 'python3 -m bandit -r ./src/main.py -f json -o ./out.json > /dev/null 2>&1'
os.system(s)
with open('out.json', 'r') as f:
    b = json.load(f)

if b['results'] or w:
    raise RuntimeError('ошибочка')
