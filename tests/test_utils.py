from src.utils import get_data, get_last_values, get_format_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_get_last_values(test_data):
    data = get_last_values(test_data)
    assert [x["date"] for x in test_data] == ['2019-12-08T22:46:21.935582', '2019-12-07T06:17:14.634890', '2019-11-19T09:22:25.899614', '2019-11-13T17:38:04.800051', '2019-11-05T12:04:13.781725']

def test_format_data(test_data):
    data = get_format_data(test_data)
    assert data == ['08.12.2019 Открытие вклада\n -> Счет **5907\n41096.24 USD\n', '07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n', '19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.\n', '13.11.2019 Перевод со счета на счет\nСчет **9794 -> Счет **8125\n62814.53 руб.\n', '05.11.2019 Открытие вклада\n -> Счет **8381\n21344.35 руб.\n']
