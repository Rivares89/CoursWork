from src.utils import get_data, get_filtr_data, get_last_values, get_format_data

def main():
    data = get_data()
    data = get_filtr_data(data)
    data = get_last_values(data)
    format_data  = get_format_data(data)
    print(format_data)
    for item in format_data:
        print(item)

if __name__ == "__main__":
    main()