# -*- coding: utf-8 -*-

from time import sleep
from os import system

from .container import Container


def main_menu():
    main_menu_list = """
    1. Добавить студента.
    2. Добавить преподавателя.
    3. Вывести список.
    4. Редактировать список.
    5. Очистить список.
    6. Удалить человека из списка.
    7. Записать список в файл.
    8. Прочитать список из файла.
    0. Выход.
    """
    system('cls')
    container = Container()
    main_menu_ans = {
            '1': container.add_list_student,
            '2': container.add_list_teacher,
            '3': container.get_list,
            '4': container.edit_list,
            '5': container.clear_list,
            '6': container.del_list,
            '7': container.write_list,
            '8': container.read_list,
            '0': main_menu
            }
    system('cls')
    print(main_menu_list)
    ans = input('Выберите пункт из списка: ')
    if ans == '0':
        system('cls')
        exit(0)
    system('cls')
    try:
        main_menu_ans[f'{ans}']()
    except KeyError:
        print('Ошибка. Попробуйте еще раз.')
        sleep(2)
        main_menu()
    main_menu()


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        exit(0)
