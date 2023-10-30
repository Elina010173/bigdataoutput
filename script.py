import csv
from datetime import datetime

def calculate_average_temperature(input_filename, output_filename):
    # Создайте словарь для хранения суммы температур и количества измерений для каждого дня
    daily_temperatures = {}

    # Открываем CSV файл для чтения
    with open(input_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            start_time_str = row['Start time']
            value = float(row['Value'])

            # Преобразовываем строку с временем в объект datetime
            current_datetime = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')

            # Извлекаем дату из объекта datetime
            current_date = current_datetime.date()

            # Проверяем, есть ли уже запись для этой даты в словаре
            if current_date in daily_temperatures:
                daily_temperatures[current_date]['sum'] += value
                daily_temperatures[current_date]['count'] += 1
            else:
                daily_temperatures[current_date] = {'sum': value, 'count': 1}

    # Открываем новый CSV файл для записи средних температур за каждый день
    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Average Temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Записываем заголовок
        writer.writeheader()

        # Записываем средние температуры за каждый день в новый файл
        for date, data in daily_temperatures.items():
            average_temperature = data['sum'] / data['count']
            writer.writerow({'Date': date, 'Average Temperature': average_temperature})

    print(f"Средние температуры за каждый день были записаны в новый CSV файл '{output_filename}'.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Calculate average temperature from a CSV file.")
    parser.add_argument("input_file", help="Input CSV file name")
    parser.add_argument("output_file", help="Output CSV file name")

    args = parser.parse_args()

    calculate_average_temperature(args.input_file, args.output_file)
