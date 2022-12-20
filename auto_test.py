import os
import json

a = os.system('python3 -m pycodestyle ./src > /dev/null 2>&1')
os.system('python3 -m bandit -r ./src/main.py -f json -o ./out.json > /dev/null 2>&1')
os.system('python3 test_app.py > test_app.txt')
os.system('python3 test_integr.py > test_integr.txt')

with open('out.json', 'r') as f:
    b = json.load(f)

with open('test_app.txt', 'r') as f:
    c = f.read().strip()

with open('test_integr.txt', 'r') as f:
    d = f.read().strip()



if b['results'] or a or not d.endswith('OK') or c.endswith('OK'):
    raise RuntimeError('ошибочка')

