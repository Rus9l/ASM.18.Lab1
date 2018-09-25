# -*- coding: utf-8 -*-

from time import sleep
from os import system

from .container import Container


def main_menu():
    """
    Функция основного меню
    """
    # основное меню
    main_menu_list = """
    1. Добавить студента.
    2. Добавить преподавателя.
    3. Вывести список.
    4. Очистить список.
    5. Удалить человека из списка.
    6. Записать список в файл.
    7. Прочитать список из файла.
    0. Выход.
    """
    system('cls')     # очистка консоли
    container = Container()
    main_menu_ans = {
            '1': container.add_list_student,
            '2': container.add_list_teacher,
            '3': container.get_list,
            '4': container.clear_list,
            '5': container.del_list,
            '6': container.write_list,
            '7': container.read_list,
            '0': main_menu
            }
    system('cls')
    print(main_menu_list)
    ans = input('Выберите пункт из списка: ')
    if ans == '0':
        exit(0)
    system('cls')
    try:
        main_menu_ans[f'{ans}']()
    except KeyError:
        print('Ошибка. Попробуйте еще раз.')
        sleep(2)
        main_menu()
    main_menu()    # возврат в меню после завершения выполнения функции


if __name__ == '__main__':
    main_menu()
