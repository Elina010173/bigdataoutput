import csv
from datetime import datetime

# Создайте словарь для хранения суммы температур и количества измерений для каждого дня
daily_temperatures = {}

# Открываем CSV файл для чтения
with open('HM_data_2013-12-18 10_42_00.csv', newline='') as csvfile:
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
with open('average_daily_temperatures.csv', 'w', newline='') as csvfile:
    fieldnames = ['Date', 'Average Temperature']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Записываем заголовок
    writer.writeheader()

    # Записываем средние температуры за каждый день в новый файл
    for date, data in daily_temperatures.items():
        average_temperature = data['sum'] / data['count']
        writer.writerow({'Date': date, 'Average Temperature': average_temperature})

print("Средние температуры за каждый день были записаны в новый CSV файл 'average_daily_temperatures.csv'.")
