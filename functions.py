def read_note_dataCSV():
    note_book_list = []
    try:
        note_data = open("NoteBook.csv", "r", encoding="utf8")
        for line in note_data:
            note_book_list.append(line)
        note_data.close()
    except FileNotFoundError:
        pass
    return note_book_list

def save_new_note_dataCSV(new_list):
    new_data = open("NoteBook.csv", "w", encoding="utf8")
    for item in new_list:
        new_data.write(item)
    new_data.close()
    
def add_new_dataCSV(notebook_list, title, body, date, time):
    note_book_list_id = []
    list_a = []
    max = 0
    with open("NoteBook.csv", "a+", encoding="utf8") as note_book:
        if notebook_list != None:
            for item in notebook_list:
                list_a = list(item.split(';'))
                note_book_list_id.append(int(list_a[0]))
                list_a.clear()
        for i in note_book_list_id:
            if i > max:
                max = i
        new_id = max + 1
        note_book.write(str(f'{new_id};{title};{body};{date};{time};\n'))
    note_book.close()
    return new_id
        
def note_view(str_note):
    note = list(str(str_note).split(';'))
    return print(f'id: {note[0]}, title: {note[1]}, body: {note[2]}, date: {note[3]}, time: {note[4]}')
    