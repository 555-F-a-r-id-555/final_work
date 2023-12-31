import csv
import path_to_file


def change_note(file_name, row_number):
    new_data = input("Введите новую заметку: ")
    try:
        data = [int(row_number) - 1,
                f"{path_to_file.get_time()[0]}",
                f"{path_to_file.get_time()[1]}",
                new_data
                ]

        path_to_file.change_or_delete(file_name, int(row_number), data)
        print(f"\033[33mЗаметка {file_name} была изменена")
    except Exception as error:
        print(f"\033[31m {error}")


# row_number_to_update = 4
# file_name = "note"
# change_note(file_name, row_number_to_update)
