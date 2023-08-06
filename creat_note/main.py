import create_note
import add_note
import change_note
import delete_note
import delete_all
import sorted_by_data_time
import read_file
import get_file_list

# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.

# Критерии оценки
# Приложение должно запускаться без ошибок, должно уметь сохранять данные
# в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять
# записку, редактировать ее и удалять.

def get_info_from_user():
    print("\033[32mВведите команду:")
    comand = input()

    match comand:
        case "Create":
            note_name = input("\033[34mВведите название файла:")
            note_data = input("\033[34mВведите содержание заметки:")
            create_note.create_note(note_name, note_data)
            read_file.get_current_note(file_name=note_name, current_num=1)
        case "Add":
            note_name = input("\033[34mВведите название файла:")
            note_data = input("\033[34mВведите новое содержание заметки:")
            add_note.add_note(note_name, note_data)
            num = read_file.get_note_number(file_name=note_name)
            read_file.get_current_note(file_name=note_name, current_num=num)
        case "Change":
            print("\033[33mЧто-бы узнать номер строки, используйте команду Show")
            note_name = input("\033[34mВведите название файла:")
            note_row_number = input("\033[34mВведите номер строки:")
            change_note.change_note(note_name, note_row_number)
            num = read_file.get_note_number(file_name=note_name)
            read_file.get_current_note(file_name=note_name, current_num=num)
        case "Delete":
            note_name = input("\033[34mВведите название файла:")
            note_row_number = input("\033[34mВведите номер строки:")
            delete_note.delete_note(note_name, note_row_number)
            num = read_file.get_note_number(file_name=note_name)
            read_file.get_current_note(file_name=note_name, current_num=num)
        case "Delete_all":
            note_name = input("\033[34mВведите название файла:")
            delete_all.delete_all(note_name)
            print(f"\033[33mЗаметка была удалена")
        case "Show":
            note_name = input("\033[34mВведите название заметки:")
            read_file.show_all(note_name)
        case "Sorted_time":
            note_name = input("\033[34mВведите название файла:")
            sorted_by_data_time.sort_by_datetime(note_name)
            num = read_file.get_note_number(file_name=note_name)
            read_file.get_current_note(file_name=note_name, current_num=num)
        case "Sorted_csv":
            note_name = input("\033[34mВведите название файла:")
            sorted_by_data_time.sort_csv(note_name)
            num = read_file.get_note_number(file_name=note_name)
            read_file.get_current_note(file_name=note_name, current_num=num)
        case "GetList":
            get_file_list.get_file_list()




get_info_from_user()
