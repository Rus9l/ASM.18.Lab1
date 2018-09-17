# -*- coding: utf-8 -*-

import pickle
from time import sleep
from os import system

from .read_write import ReadWrite
from .main_class import MainClass


class Container(ReadWrite):
    """
    Контейнерный класс
    """
    students = []

    def __init__(self):
        self.group = None

    def add_list(self):
        """
        Добавление новых записей в список
        """
        r = ReadWrite()
        mc = MainClass()
        mc.name = input('Введите имя: ')
        mc.age = input('Введите возраст: ')
        r.number = input('Введите телефон: ')
        self.group = input('Введите номер группы: ')
        self.students.append(f'Имя:{mc.name}, Возр:{mc.age}, Группа:{self.group}, Тел:{r.number}')
        system('clear')
        print(f'\n{mc.name} добавлен в список.')
        sleep(2)   # пауза 2 секунды перед выходм в меню

    def get_list(self):
        """
        Вывод списка
        """
        if self.students == []:
            print('Список пуст.\n')
        else:
            print(self.students)
        input('Для продолжения нажмите ENTER')  # задержка возврата в меню

    def read_list(self):
        """
        Чтение списка из файла
        """
        list_file = input('Введите имя файла, который хотите открыть: ')
        try:
            lst = open(f'st26/{list_file}', 'rb')
            r_list = pickle.load(lst)
            print(r_list)
            lst.close()
            sleep(5)
        except FileNotFoundError:
            print(f'Файл {list_file} не найден.')
            Container().read_list()

    def write_list(self):
        """
        Запись списка в файл
        """
        list_file = input('Введите имя для сохраняемого списка: ')
        l_file = open(f'st26/{list_file}', 'wb')
        pickle.dump(self.students, l_file, 2)
        print(f'\nФайл сохранен {list_file}')
        sleep(2)

    def clear_list(self):
        """
        Очистка списка
        """
        q = input('Вы уверены, что хотите очистить список? (Н/д): ').lower()
        if q == 'д' or q == 'y' or q == 'да' or q == 'yes':
            self.students.clear()
            print('Список очищен.')
            sleep(2)
        else:
            print('Отмена.')
            sleep(2)


if __name__ == '__main__':
    pass
