def show_records(phones: str):
    with open(phones, 'r', encoding='utf-8') as file:
        for user_info in file:
            print(*user_info.split('_'), sep=" ")


def new_records(phones: str):
    with open(phones, 'r+', encoding='utf-8') as file:
        record_id = 0
        for user_info in file:
            if user_info != '':
                record_id += 1
        print(
            'Введите фамилию, имя, отчество и номер телефона через пробел, после ввода нажмите клавишу enter: '
        )
        user_info = f'{int(record_id) + 1}_' + '_'.join(
            input().split()[:4]) + '_\n'
        file.write(user_info)


def find_records():
    print('Выберите что будете искать: ')
    print(
        '1 - id, 2 - Фамилия, 3 - Имя, 4 - Отчество, 5 - Номер телефона, 0 - Выход'
    )
    user_inp = input()
    while user_inp not in ('1', '2', '3', '4', '5', '0'):
        print('Ошибка, введите правильное значение: ')
        print(
            '1 - id, 2 - Фамилия, 3 - Имя, 4 - Отчество, 5 - Номер телефона, 0 - Выход'
        )
        user_inp = input()
    if user_inp != '0':
        inout = input('Введите данные: \n')
        return inout
    else:
        return '0', '0'


def find_more_records(phones: str, inout):
    if inout != '0':
        found = False
        with open(phones, 'r', encoding='utf-8') as file:
            for user_info in file:
                find_info = user_info.split('_')
                if inout in find_info:
                    print(*user_info.split('_'), sep=" ")
                    found = True
        if not found:
            print("Такого значения нет.")
        return found


def replace_record(phones: str, id_record, replaced_user_info: str):
    replaced = ''
    with open(phones, 'r', encoding='utf-8') as file:
        for user_info in file:
            replaced += user_info
            if id_record == user_info.split('_', 1)[0]:
                replaced = replaced.replace(user_info, replaced_user_info)
    with open(phones, 'w', encoding='utf-8') as data:
        data.write(replaced)


def change_records(phones: str):
    id_record = input('Введите id: ')
    if id_record != '0':
        replaced_line = f'{int(id_record)}_' + '_'.join(
            input(
                'Введите фамилию, имя, отчество и номер телефона через пробел, после ввода нажмите клавищу enter: \n'
            ).split()[:4]) + '_\n'
        replace_record(phones, id_record, replaced_line)


def delete_records(phones: str):
    id_record = input('Введите id: ')
    if id_record != '0':
        replace_record(phones, id_record, '')


phones = r'Phone_directory.txt'

try:
    file = open(phones, 'r')
except IOError:
    print('Новый телефонный справочник создан (Phone_directory.txt)')
    file = open(phones, 'w')
finally:
    file.close()

acts = {
    '1': 'Открыть данные справочника',
    '2': 'Новая запись',
    '3': 'Поиск',
    '4': 'Изменить данные',
    '5': 'Удалить данные',
    '0': 'Выход'
}

act = None
while act != '0':
    print('Выберите нужный пункт меню: ', *[f'{i} - {acts[i]}' for i in acts])
    act = input()
    while act not in acts:
        print('Выберите нужный пункт меню: ',
              *[f'{i} - {acts[i]}' for i in acts])
        act = input()
        if acts not in acts:
            print('Ошибка, введены неверные данные!')
    if act != '0':
        if act == '1':
            show_records(phones)
        elif act == '2':
            new_records(phones)
        elif act == '3':
            find_more_records(phones, *find_records())
        elif act == '4':
            change_records(phones)
        elif act == '5':
            delete_records(phones)
