# -*- coding: utf-8 -*-
from group import Office

u = Office()

MENU_OPTIONS = [
    ('Добавить устройство', u.add_device),
    ('Добавить смартфон', u.add_smartphone),
    ('Изменить данные по устройству', u.edit_list),
    ('Вывести список устройств', u.print_list),
    ('Сохранить в файл', u.save_to_file),
    ('Загрузить из файла', u.load_from_file),
    ('Удалить устройство', u.delete_from_list),
    ('Очистить всех', u.clear)
]


def main():

    while True:
        
        print('------------------------------')
        
        for i, item in enumerate(MENU_OPTIONS, start = 1):
            print('{0}: {1}'.format(i, item[0]))
        print('0: Выход')

        print('------------------------------')


        try:
            choice = int(input('>> '))

            if choice == 0:
                break

            MENU_OPTIONS[choice - 1][1]()
        
        except Exception as ex:
            print(ex)
            print('Ошибка!')