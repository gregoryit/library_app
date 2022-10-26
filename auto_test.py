import os
import json

a = os.system('pycodestyle ./src > /dev/null 2>&1')
os.system('bandit -r ./src -f json -o out.json > /dev/null 2>&1')

with open('out.json', 'r') as f:
    b = json.load(f)

if b['results'] or a:
    raise

