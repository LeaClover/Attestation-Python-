from text import create, update_by_keyword, list_notes, update_by_id, delete_by_id, delete_by_keyword
from text import find_by_id, find_by_keyword, date_note
 
def start():
    print('***Привет, это приложение для заметок!***\nЧто вы хотите сделать?\n')
    command = command_list()
    match str.upper(command):
        case 'ADD' | 'AD' | 'A':
            create()
            continue_note_book()
        case 'UPDATE' | 'UPD' | 'U':
            comm = update_comm()
            if comm == 0:
                update_by_id()
            elif comm == 1:
                update_by_keyword()
            continue_note_book()
        case 'LIST' | 'LI' | 'L':
            list_notes()
            continue_note_book()
        case 'DELETE' | 'DEL' | 'D':
            comm = update_comm()
            if comm == 0:
                delete_by_id()
            elif comm == 1:
                delete_by_keyword()
            continue_note_book()
        case 'FIND' | 'FI' | 'F':
            comm = update_comm()
            if comm == 0:
                find_by_id()
            elif comm == 1:
                find_by_keyword()
            continue_note_book()
        case 'DATE' | 'DT':
            date_note()
            continue_note_book()
        case 'COMMAND' | 'COM' | 'C':
            command_list()
        case 'EXIT' | 'EX' | 'E':
            exit()
        case _:
            print('Команда не найдена! Попробуйте заново!')
            start()
            
def continue_note_book():
    print('Продолжить работу?\nY -- да\nN -- нет')
    com = input()
    if str.upper(com) == 'Y' or str.upper(com) == "YES":
        start()
    elif str.upper(com) == "N" or str.upper(com) == "NO":
        exit()
    else:
        print('Введена неверная команда!')
        continue_note_book()
        
def command_list():
    print('Список команд: \nADD -- создать новую заметку\nUPDATE -- внести изменения в существующую заметку\n'
          'LIST -- показать список заметок\nDELETE -- удалить заметку\nFIND -- найти конкретную заметку\n'
          'DATE -- показать список заметок по дате\nCOMMAND -- список команд\nEXIT -- завершение работы\n')
    command = input('Введите команду: ')
    return command
    
def update_comm():
    print('ID -- поиск по id\nKEY -- поиск по ключевому слову\nMAIN -- выход в главное меню\nEXIT -- выйти')
    comm = input('Введите команду для поиска: ')
    match str.upper(comm):
        case 'ID' | 'I':
            return 0
        case 'KEY' | 'K':
            return 1
        case 'EXIT' | 'E':
            exit()
        case 'MAIN' | 'M':
            start()
        case _:
            print('Введена неверная команда! Попробуйте снова!')
            update_comm()
