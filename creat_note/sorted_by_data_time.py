import csv
import path_to_file


def sort_by_datetime(file_name):
    try:
        path_to_note = path_to_file.get_path_to_file(path_to_file.directory_name, file_name)
        with open(path_to_note, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file, delimiter="/")
            header = next(reader)
            rows = list(reader)

        sorted_rows = sorted(rows, key=lambda row: (row[1], row[2]))

        with open(path_to_note, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter="/")
            writer.writerow(header)
            writer.writerows(sorted_rows)
            print(f"\033[33mЗаметка {file_name} была отсортирована")
    except FileNotFoundError as error:
        print(f"\033[31m {error}")
    except Exception as ex:
        print(f"\033[31m {ex}")


def sort_csv(file_name):
    try:
        path_to_note = path_to_file.get_path_to_file(path_to_file.directory_name, file_name)
        with open(path_to_note, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file, delimiter="/")
            rows = [row for row in reader if any(field.strip() for field in row)]

        sorted_rows = sorted(rows, key=lambda row: (row[1], row[2]))

        with open(path_to_note, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter="/")
            writer.writerows(sorted_rows)
            # print(f"\033[33mЗаметка {file_name} была отсортирована")
    except Exception as ex:
        print(f"\033[31m {ex}")


# file_name = "note2"
# sort_csv(file_name)
