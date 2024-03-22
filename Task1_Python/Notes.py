def interface():
    with open('notes.txt', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '5':
        print('Возможные варианты взаимодействия:\n'
            '1. Просмотреть заметки\n'
            '2. Добавить заметку\n'
            '3. Редактировать заметку\n'
            '4. Удлаить заметку\n'
            '5. Выход из программы')
        
        command = input('Введите пункт меню: ')
        
        while command not in ('1', '2', '3', '4', '5'):
            print('Некорретные данные')
            command = input('Введите пункт меню: ')

        match command:
            case '1':   
                print('1')
            case '2':   
                print('2')                
            case '3':   
                print('3')
            case '4':   
                print('4')
            case '5':   
                print('Всего хорошего!')
interface()