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
        loaded_data = pd.read_csv(file_path)
        # Вызов функции для обработки данных
        display_data_for_last_24_hours(file_path)

# Функция для вывода данных за сутки
def display_data_for_last_24_hours(file_path):
    if loaded_data is not None:
        import csv
        from datetime import datetime

        # Ваш код для обработки CSV файла, используя file_path
        pass
    else:
        print("CSV файл не загружен.")

# Функция для вывода среднесуточной температуры
def display_average_daily_temperature():
    if loaded_data is not None:
        new_window = tk.Toplevel()
        new_window.title("Среднесуточная температура")
        average_temperature = loaded_data['temperature'].mean()
        text_widget = tk.Text(new_window)
        text_widget.insert(tk.END, f"Среднесуточная температура: {average_temperature:.2f} °C")
        text_widget.pack()
    else:
        print("CSV файл не загружен.")

# Функция для открытия CSV файла в Excel
def open_csv_in_excel():
    if loaded_data is not None:
        loaded_data.to_csv('data.csv', index=False)  # Сохраняем данные в CSV файл
        subprocess.Popen(['start', 'excel', 'data.csv'], shell=True)

if __name__ == "__main__":
    # Создаем главное окно
    window = tk.Tk()
    window.title("Вывод данных файлов")

    # Создаем кнопки
    button_load_csv = tk.Button(window, text="Загрузить CSV файл", command=load_csv_file)
    button_display_temperature = tk.Button(window, text="Вывести среднесуточную температуру", command=display_average_daily_temperature)
    button_open_in_excel = tk.Button(window, text="Открыть в Excel", command=open_csv_in_excel)

    # Размещаем кнопки на окне
    button_load_csv.pack()
    button_display_temperature.pack()
    button_open_in_excel.pack()

    # Запускаем главный цикл приложения
    window.mainloop()
