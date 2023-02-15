from logCSV import create_note, list_all_notes, find_notes_by_date, delete_note_by_id, delete_note_by_keyword
from logCSV import find_note_by_id, find_note_by_keyword
from datetime import datetime

def create():
    title = input('Заголовок: ')
    body = input('Содержание заметки: ')
    current_date = datetime.now()
    day = current_date.day
    month = current_date.month
    year = current_date.year
    date = str.format('{}.{}.{}'.format(day, month, year))
    time = str.format('{}:{}:{}'.format(datetime.now().hour, datetime.now().minute, datetime.now().second))
    create_note(title, body, date, time)
    print('Элемент добавлен')
  
def update_by_id():
    try:
        find_id = int(input('Введите id: '))
        key = delete_note_by_id(find_id)
        if key == 1:
            update_success()
    except ValueError:
        print('Введено неверное значение! Введите номер ID!')
        update_by_id()

def update_by_keyword():
    find_keyword = input('Введите ключевое слово: ')
    key = delete_note_by_keyword(find_keyword)
    if key == 1:
        update_success()
     
def update_success():
    print('Внесите изменения!')
    create()
    print('Запись обновлена!')

def delete_by_id():
    try:
        find_id = int(input('Введите id: '))
        key = delete_note_by_id(find_id)
        if key == 1:
            print('Заметка успешно удалена!')
    except ValueError:
        print('Введено неверное значение. Введите номер ID!')
        delete_by_id()
    
def delete_by_keyword():
    keyword = input('Введите ключевое слово: ')
    key = delete_note_by_keyword(keyword)
    if key == 1:
        print('Заметка успешно удалена!')

def find_by_id():
    try:
        find_id = int(input('Введите id: '))
        flag = find_note_by_id(find_id)
        if flag == 1:
            print('--DONE--')
    except ValueError:
        print('Введено неверное значение. Введите номер ID!')
        find_by_id()
        
def find_by_keyword():
    keyword = input('Введите ключевое слово: ')
    note = find_note_by_keyword(keyword)
    if note != None:
            print('--DONE--')
    if note == None:
        print('Что-то пошло не так!')
  
def list_notes():
    print('Все активные заметки: \n')
    list_all_notes()
   
def date_note():
    print('Введите дату для поиска заметок: ')
    try:
        day = int(input('День: '))
        month = int(input('Месяц: '))
        year = int(input('Год: '))
        print('Список заметок по выбранной дате: ')
        find_notes_by_date(day, month, year)
    except ValueError:
        print('Неверный формат ввода, введите числа!')
        date_note()
        