from utils import get_data, get_filtr_data, get_last_values

def main():
    data = get_data()
    data = get_filtr_data(data)
    data = get_last_values(data)
    for count in data:
        print (count['date'])
    # print (data[1])


if __name__ == "__main__":
    main()