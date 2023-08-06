import csv
import os
import time

directory_name = "notes"


def get_path_to_file(directory_name, file_name):
    file_name = file_name + ".csv"
    path_to_note = os.path.join(directory_name, file_name)
    return path_to_note


def check_file(path):
    return os.path.exists(path)


def check_directory(directory_name):
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)


def get_time():
    date_now = time.strftime("%Y.%m.%d")
    time_now = time.strftime("%H:%M:%S")
    list1 = [date_now, time_now]
    return list1


def change_or_delete(file_name, row_number, data):
    try:
        path_to_note = get_path_to_file(directory_name, file_name)
        with open(path_to_note, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file, delimiter="/")
            rows = list(reader)

        if 1 < int(row_number) <= len(rows):
            rows[int(row_number) - 1] = data

            with open(path_to_note, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file, delimiter="/")
                writer.writerows(rows)
            if data == ():
                print(f"\033[33mЗаметка под номером {row_number} была удалена")
        else:
            print(f"\033[31mНекорректный номер строки, номер строки должен быть больше 1")
    except FileNotFoundError as error:
        print(f"\033[31m {error}")
    except Exception as error:
        print(f"\033[31m {error}")
