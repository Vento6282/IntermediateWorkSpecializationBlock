import datetime

def show_notes():
    with open('notes.csv', 'r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n')
        if notes_list[0] == '':
            print('Заметок нет!')
        else:
            print(delimer)
            print('Список заметок:\n')
            for note in notes_list:
                show_note(note)

def show_note(note):
    parse_note = note.split(';')
    print('ID: ' + parse_note[0] + '; Дата создания: ' + parse_note[3] + '; Дата изменения: ' + parse_note[3] + '\n'
          'Тема: ' + parse_note[1] + '\n'
          'Текст: ' + parse_note[2] + '\n')

def add_note():
    print(delimer)
    check = True
    while (check):
        subject = input('Введите тему заметки: ')
        check = check_symbol(subject)
        if (check):
            print('Тема заметки не должна содержать символ ";" !')
    check = True        
    while (check):    
        body = input('Введите текст заметки: ')
        check = check_symbol(body)
        if (check):
            print('Текст заметки не должен содержать символ ";" !')
    answer = ''
    while(answer != 'y' and  answer != 'n'):
        print(delimer)
        print('Тема: ' + subject + '\n'
              'Текст: ' + body)
        answer = input('Добавить заметку? y/n \n')
        if (answer == 'y'):
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note = str(new_index()) + ';' + subject + ';' + body + ';' + str(now) + ';' + str(now) + '\n'
            write_note(note)
            print('Заметка добавлена!')    
        elif(answer == 'n'):
            print('Создание заметки отменено!')
        else:
            print('Некорретные данные')

def write_note(note):
    with open('notes.csv', 'a', encoding='UTF-8') as file:
        file.write(note)

def check_symbol(word):
    if (word.find(';') == -1):
        return False
    else:
        return True

def new_index():
 with open('notes.csv', 'r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n')
        if notes_list[0] == '':
            return 1
        else:
            new_index = 0
            for note in notes_list:
                index = int(note.split(';')[0])
                if index > new_index:
                    new_index = index
            return new_index + 1

def edit_note():
    print(delimer)
    with open('notes.csv', 'r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n')
    if(notes_list[0] == ''):
        print('Список заметок пуст! Редактирование невозможно!')
    else:
        show_notes()
        input_id = -1
        while input_id == -1:
            print('0. Выход в главное меню')
            input_id = input('Введите ID записи, которую необходимо редактровать:\n')
            if(input_id == '0'):
                print('Редактирование заметки отменено!')
                return
            input_id = check_id(notes_list, input_id)
        input_object = -1
        while input_object not in ('1', '2', '0'):
            print(delimer)
            show_note(notes_list[input_id])     
            print('1. Тема\n'
                '2. Текст\n'
                '0. Выход в главное меню')
            input_object = input('Введите пункт меню, что необходимо изменить в заметке:\n')  
            if (input_object == '0'):
                print('Редактирование отменено!')
                return 
            if(input_object not in('1','2')):
                print('Некорректные данные!')
        input_text = ''
        if(input_object == '1'):
            check = True
            while (check):    
                print(delimer)
                input_text = input('Текущая тема заметки:' + notes_list[input_id].split(';')[1] + '\nВведите новую тему заметки:\n')
                check = check_symbol(input_text)
                if (check):
                    print('Текст заметки не должен содержать символ ";" !')
                
            answer = ''
            while(answer != 'y' and  answer != 'n'):   
                print(input_text)         
                answer = input('Заменить тему заметки с "' + notes_list[input_id].split(';')[1] + '" на "' + input_text + '"? y/n \n')
                if (answer == 'y'):
                    notes_list[input_id].split(';')[1] = 'Заглушка'
                    
                    print('Тема заметки изменена')
                    print(*notes_list)
                elif(answer == 'n'):
                    print('Редактирование заметки отменено!')
                else:
                    print('Некорретные данные')
            with open('notes.csv', 'w', encoding='UTF-8') as file:
                file.write('\n'.join(notes_list) + '\n')  


        if(input_object == '2'):
            while (check):
                print(delimer)
                input_text = input('Текущий текст заметки: ' + notes_list[input_id].split(';')[2] + '\nВведите новый текст заметки:\n')
                check = check_symbol(input_text)
                if (check):
                    print('Текст заметки не должен содержать символ ";" !')
        


        






def delete_note():
    print(delimer)
    with open('notes.csv', 'r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n')
    if(notes_list[0] == ''):
        print('Список заметок пуст! Удаление невозможно!')
    else:
        show_notes()
        input_id = -1
        while input_id == -1:
            print('0. Выход в главное меню')
            input_id = input('Введите ID записи, которую необходиом удалить:\n')
            if(input_id == '0'):
                print('Удаление заметки отменено!')
                return
            input_id = check_id(notes_list, input_id)

        answer = ''
        while(answer != 'y' and  answer != 'n'):
            print(delimer)
            show_note(notes_list[input_id])
            answer = input('Удалить заметку? y/n \n')
            if (answer == 'y'):
                notes_list.pop(input_id)
                with open('notes.csv', 'w', encoding='UTF-8') as file:
                    file.write('\n'.join(notes_list) + '\n')   
                print('Заметка удалена!')    
            elif(answer == 'n'):
                print('Удаление заметки отменено!')
            else:
                print('Некорретные данные')
        with open('notes.csv', 'w', encoding='UTF-8') as file:
            file.write('\n'.join(notes_list) + '\n')   

def check_id(notes_list, input_id):
    check_id = -1
    for i in range(len(notes_list)):
        if(notes_list[i].split(';')[0] == input_id):
            check_id = i
    if(check_id == -1):
                show_notes()
                print('Заметки с ID = "' + input_id + '" нет!')
    return check_id

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

delimer = '-------------------------------'

interface()
