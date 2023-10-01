import json

from datetime import datetime

def get_data():
    with open ('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_filtr_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data

def get_last_values(data):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:5]
    return data
