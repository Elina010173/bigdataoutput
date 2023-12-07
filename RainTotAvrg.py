import csv
from datetime import datetime

def calculate_daily_precipitation(input_filename, output_filename):
    data_by_date = {} 

    with open(input_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            start_time_str = row['Start time']
            value = float(row['Value'])

            current_date = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S').date()

            if current_date in data_by_date:
                data_by_date[current_date] += value
            else:
                data_by_date[current_date] = value

    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Year', 'Month', 'Day', 'precipitation total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for date, total_precipitation in data_by_date.items():
            record = {
                'Year': date.year,
                'Month': date.month,
                'Day': date.day,
                'precipitation total': round(total_precipitation, 2) 
            }

          
            formatted_record = {key: str(value).ljust(15) for key, value in record.items()}

            writer.writerow(formatted_record)

    print(f"Сумма количества осадков за каждый день была записана в новый CSV файл '{output_filename}'.")

if __name__ == "__main__":
    input_filename = input("Введите полный путь к входному CSV файлу: ")
    output_filename = input("Введите имя выходного CSV файла: ")

    calculate_daily_precipitation(input_filename, output_filename)
