import json

from datetime import datetime

def get_data():
    with open ('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_filtr_data(data):
    data = [x for x in data if 'state' in x and x.get('state') == 'EXECUTED']
    return data

def get_last_values(data):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:5]
    return data

def get_format_data(data):
    format_data = []
    for count in data:
        date = datetime.strptime(count['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = count['description']
        from_ = from_to(count, 'from')
        to_ = from_to(count, 'to')
        amount = f"{count['operationAmount']['amount']} {count['operationAmount']['currency']['name']}"
        format_data.append(f'{date} {description}\n{from_} -> {to_}\n{amount}')
    return format_data

def from_to(count, from_or_to):
    if count.get(from_or_to):
        from_list = count.get(from_or_to).split(" ")
        if from_list[0] == "Счет":
            from_info = f"Счет **{from_list[1][-4:]}"
        else:
            from_info = " ".join(
                from_list[:-1]) + f' {from_list[-1][:4]} {from_list[-1][4:6]}** **** {from_list[-1][-4:]}'
    else:
        from_info = ""
    return  from_info
#
#
#
# # Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.

