import pytest
from utils import get_data, get_filtr_data, get_last_values, get_format_data

def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_get_last_values(test_data):
    data = get_last_values(test_data)
    assert [x["date"] for x in data] == []