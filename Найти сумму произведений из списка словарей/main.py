# TODO решите задачу

import json

def task() -> float:
    filename = 'input.json'
    sum = 0
    with open(filename) as file:
        data = json.load(file)
    for dicts in data:
        product = dicts['score'] * dicts['weight']
        sum += product
    return round(sum, 3)



print(task())
