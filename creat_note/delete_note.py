import path_to_file


def delete_note(file_name, row_number):
    data = ()


    path_to_file.change_or_delete(file_name, row_number, data)
    # print(f"\033[33mЗаметка под номером {row_number} была удалена")


# row_number_to_update = 30
# file_name = "note"
# delete_note(file_name, row_number_to_update)
