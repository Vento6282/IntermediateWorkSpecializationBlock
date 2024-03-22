import datetime

delimer = '-------------------------------'

def show_notes():
    with open('notes.csv', 'r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n')
        if notes_list[0] == '':
            print('Заметок нет!')

        else:
            print(delimer)
            print('Список заметок:\n')
            for note in notes_list:
                parse_note(note)
            print(delimer)

def parse_note(note):
    parse_note = note.split(';')
    print('ID: ' + parse_note[0] + '; Дата создания: ' + parse_note[3] + '; Дата изменения: ' + parse_note[3] + '\n'
          'Тема: ' + parse_note[1] + '\n'
          'Текст: ' + parse_note[2] + '\n')

def interface():
    with open('notes.csv', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '5':
        print('Возможные действия:\n'
            '1. Просмотреть заметки\n'
            '2. Добавить заметку\n'
            '3. Редактировать заметку\n'
            '4. Удалить заметку\n'
            '5. Выход из программы')
        
        command = input('Введите пункт меню: ')
        
        while command not in ('1', '2', '3', '4', '5'):
            print('Некорретные данные')
            command = input('Введите пункт меню: ')

        match command:
            case '1':   
                show_notes()
            case '2':   
                print('2')                
            case '3':   
                print('3')
            case '4':   
                print('4')
            case '5':   
                print('Всего хорошего!')
interface()

# идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.


 
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now)
