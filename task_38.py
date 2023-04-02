# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

def show_info():
    with open( 'phone_book.txt' , 'r' ) as file:
        book = file.read().split('\n')
    print(book)

def new_string():
    with open( 'phone_book.txt' , 'a') as file:
        file.write(input('Введите новую строку: '))

def find_info():
    with open( 'phone_book.txt' , 'r') as file:
        book = file.read().split('\n')
        t = input('Что вы хотите найти?   ')
        for i in book:
            if t in i:
                print(i)

def delete_info(name):
    persons = (open('phone_book.txt', 'r'))
    persons.read()
    with open( 'phone_book.txt' , 'w') as file:
        for person in persons:
            if name != person:
                file.write(person.split())

def change_info(new_name, old_name):
    persons = (open('phone_book.txt', 'r'))
    persons.read()
    with open("phone_book.txt", "w", ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")



while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-поиск, 1-показать справочник, 2-добавление в справочник, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(show_info())
    elif mode == '0':
        find_info()
    elif mode == '2':
        new_string()
    elif mode == '3':
        name = input('Введите имя кого удалить?: ')
        delete_info(name)
    elif mode == '4':
        old_name = input('Введите имя кого переименовать?: ')
        new_name = input('Ввелите новое имя: ')
        change_info(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('No mode')

