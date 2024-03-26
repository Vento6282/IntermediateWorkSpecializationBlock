from methods import *

def interface():
    with open('notes.csv', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '0':
        print(delimer)
        print('Возможные действия:\n'
            '1. Просмотреть заметки\n'
            '2. Добавить заметку\n'
            '3. Редактировать заметку\n'
            '4. Удалить заметку\n'
            '0. Выход из программы')
        
        command = input('Введите пункт меню: ')
        
        if (command not in ('1', '2', '3', '4', '0')):
            print('Некорретные данные')

        match command:
            case '1':   
                show_notes()
            case '2':    
                add_note()            
            case '3':   
                edit_note()
            case '4':   
                delete_note()
            case '0':   
                print(delimer)
                print('До новых встреч!')

delimer = '------------------------------------------'

interface()
