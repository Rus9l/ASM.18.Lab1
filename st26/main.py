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
    1. Добавить новый объект.
    2. Вывести список.
    3. Очистить список.
    4. Записать список в файл.
    5. Прочитать список из файла.
    0. Выход.
    """
    system('clear')     # очистка консоли
    container = Container()
    main_menu_ans = {
            '1': container.add_list,
            '2': container.get_list,
            '3': container.clear_list,
            '4': container.write_list,
            '5': container.read_list,
            '0': main_menu
            }
    system('clear')
    print(main_menu_list)
    ans = input('Выберите пункт из списка: ')
    if ans == '0':
        exit(0)
    system('clear')
    try:
        main_menu_ans[f'{ans}']()
    except KeyError:
        print('Ошибка. Попробуйте еще раз.')
        sleep(2)
        main_menu()
    main_menu()    # возврат в меню после завершения выполнения функции


if __name__ == '__main__':
    main_menu()
