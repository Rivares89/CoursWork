from src.utils import get_data, get_filtr_data, get_last_values, get_format_data

def main():
    data = get_data() # получает данные
    data = get_filtr_data(data)  # фильтр по ключу state
    data = get_last_values(data) # берет последние 5 операций
    format_data  = get_format_data(data) # формирует отчет
    for item in format_data:
        print(item)

if __name__ == "__main__":
    main()