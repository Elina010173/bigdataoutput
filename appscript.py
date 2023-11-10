import tkinter as tk
from tkinter import filedialog
import pandas as pd
import subprocess
import csv
from datetime import datetime
import argparse

# Глобальная переменная для хранения загруженных данных
loaded_data = None

# Функция для загрузки CSV файла
def load_csv_file():
    global loaded_data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        loaded_data = pd.read_csv(file_path, iterator=True, chunksize=10000)

# Функция для вывода данных за сутки
def display_daily_data():
    global loaded_data  # Используем глобальную переменную loaded_data

    if loaded_data is not None:
        # Создайте словарь для хранения данных за каждый день
        daily_data = {}

        for chunk in loaded_data:
            for index, row in chunk.iterrows():
                start_time_str = row['Start time']
                value = float(row['Value'])

                
                current_datetime = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')

                # Извлекаем дату из объекта datetime
                current_date = current_datetime.date()

                # Проверяем, есть ли уже запись для этой даты в словаре
                if current_date in daily_data:
                    daily_data[current_date].append(value)
                else:
                    daily_data[current_date] = [value]

        # Открываем новый CSV файл для записи данных за каждый день
        output_filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if output_filename:
            with open(output_filename, 'w', newline='') as csvfile:
                fieldnames = ['Date', 'Data']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Записываем заголовок
                writer.writeheader()

                # Записываем данные за каждый день в новый файл
                for date, data in daily_data.items():
                    writer.writerow({'Date': date, 'Data': data})

            print(f"Данные за каждый день были записаны в новый CSV файл '{output_filename}'.")

# Функция для открытия CSV файла в Excel
def open_csv_in_excel():
    global loaded_data  # Используем глобальную переменную loaded_data

    if loaded_data is not None:
        # Сохраняем данные во временный CSV файл
        temp_filename = 'temp_data.csv'
        loaded_data.to_csv(temp_filename, index=False)

        # Открываем временный CSV файл в Excel
        subprocess.Popen(['start', 'excel', temp_filename], shell=True)

if __name__ == "__main__":
    # Создаем главное окно
    window = tk.Tk()
    window.title("Вывод данных файлов")

    # Создаем кнопку для загрузки CSV файла
    button_load_csv = tk.Button(window, text="Загрузить CSV файл", command=load_csv_file)
    button_load_csv.pack()

    # Создаем кнопку для вывода данных за сутки
    button_display_data = tk.Button(window, text="Вывести данные за сутки", command=display_daily_data)
    button_display_data.pack()

    # Создаем кнопку для открытия CSV файла в Excel
    button_open_in_excel = tk.Button(window, text="Открыть в Excel", command=open_csv_in_excel)
    button_open_in_excel.pack()

    # Запускаем главный цикл приложения
    window.mainloop()
