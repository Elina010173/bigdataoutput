import csv
from datetime import datetime, timedelta

data_to_write = []  # Создаем список для данных, которые будут записаны

# Открываем CSV файл для чтения
with open('HM_data_2013-12-18 10_42_00.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    prev_date = None  # Переменная для хранения предыдущей даты
    
    for row in reader:
        start_time_str = row['Start time']
        value = float(row['Value'])
        
        # Преобразовываем строку с временем в объект datetime
        current_date = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S').date()
        
        # Проверяем, если дата такая же, как и предыдущая, пропускаем запись
        if prev_date is not None and current_date == prev_date:
            continue
        
        # Создаем запись для записи в CSV файл
        record = {
            'Год': current_date.year,
            'Месяц': current_date.month,
            'День': current_date.day,
            'Температура': value
        }
        
        data_to_write.append(record)
        
        # Устанавливаем текущую дату как предыдущую для следующей итерации
        prev_date = current_date

# Открываем новый CSV файл для записи с использованием кодировки UTF-8
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Год', 'Месяц', 'День', 'Температура']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for record in data_to_write:
        writer.writerow(record)

print("Данные с одинаковыми датами были удалены, и оставшиеся данные записаны в новый CSV файл 'output.csv'.")
