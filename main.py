from datetime import datetime
import datetime


filename = 'Notes.txt'


def addNote(note, file):
    f = open(file, 'r')
    data = f.read()
    if len(data) != 0:
        data = data + '\n\n'
    now = datetime.datetime.now()
    date_time_str = now.strftime("%d/%m/%Y")
    note = "Note: " + note + ' ' + date_time_str
    data = data + note
    f = open(file, 'w')
    f.write(data)
    f.close()


def readDayNote(date, file):
    f = open(file, 'r')
    data = f.read()
    the_list = data.split('\n\n')
    new_list = []
    for i in the_list:
        if date in i:
            new_list.append(i)
    if len(new_list) != 0:
        return new_list
    return ("No notes that day")


def readAllNotes(file):
    f = open(file, 'r')
    data = f.read()
    the_list = data.split('\n\n')
    return the_list


def deleteNote(date, file):
    f = open(file, 'r')
    data = f.read()
    the_list = data.split('\n\n')
    new_list = []
    for i in the_list:
        if date in i:
            new_list.append(i)
    if len(new_list) == 0:
        print(f"No notes at this day")
    elif len(new_list) == 1:
        the_list.remove(new_list[0])
        data = '\n\n'.join(the_list)
        f = open(file, 'w')
        f.write(data)
        f.close()
    elif len(new_list) > 1:
        count = 1
        for i in new_list:
            print(str(count) + '-> ', i, end='\n')
            count += 1
        to_delete = int(input("Choose note to delete: "))
        the_list.remove(new_list[to_delete-1])
        data = '\n\n'.join(the_list)
        f = open(file, 'w')
        f.write(data)
        f.close()


while True:
    print("1) add note\n2) read day note\n3) read all\n4) delete note")
    index = input("Choose option: ")
    if index == '1':
        note = input("Enter note please:\n")
        addNote(note, filename)
    elif index == '2':
        day = input("Enter day in this format \"dd/mm/yyyy\": ")
        print(readDayNote(day, filename))
    elif index == '3':
        print(readAllNotes(filename))
    elif index == '4':
        day = input("Enter day in this format \"dd/mm/yyyy\": ")
        deleteNote(day, filename)
    elif index == 'end':
        print('Good bye!')
        break

# deleteNote(date, filename)
# print(readAllNotes(filename))
# print(readDayNote(date, filename))
# addNote("This iss my first note", filename)



