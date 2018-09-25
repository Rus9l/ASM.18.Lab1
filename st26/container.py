# -*- coding: utf-8 -*-

import pickle
from time import sleep
from os import system

from .teacher import TeacherCl
from .student import StudentCl


class Container(TeacherCl):

    db = []

    def __init__(self):
        self.name = None

    def add_list_student(self):
        """
        Добавление студента в список
        """
        st = StudentCl()
        print('Заполните данные:')
        self.name = input('ФИО: ')
        st.read_from_console()
        self.db.append(f'ФИО: {self.name}, Возраст: {st.age}, Группа: {st.group}')
        system('cls')
        print(f'\n{self.name} добавлен в список.')
        sleep(2)   # пауза 2 секунды перед выходм в меню

    def add_list_teacher(self):
        """
        Добавление преподавателя в список
        """
        tch = TeacherCl()
        print('Заполните данные:')
        self.name = input('ФИО: ')
        tch.read_from_console()
        self.db.append(f'ФИО: {self.name}, Кафедра: {tch.tchr}')
        system('cls')
        print(f'\n{self.name} добавлен в список.')
        sleep(2)

    def get_list(self):
        """
        Вывод списка
        """
        if self.db == []:
            print('Список пуст.\n')
        else:
            i = 0
            x = 1
            while x <= len(self.db):
                print(f'{i+1}. ' + self.db[i])
                x += 1
                i += 1
        input('\nДля продолжения нажмите ENTER')  # задержка возврата в меню

    def del_list(self):
        c = Container()
        c.get_list()
        try:
            target = int(input('Введите номер удаляемого человека: '))
            if target > len(self.db):
                print('В списке нет такого номера.')
                sleep(0.5)
                system('cls')
                c.del_list()
            else:
                self.db.pop(target)
        except ValueError:
            print('Необходимо ввести номер.')
            sleep(0.5)
            system('cls')
            c.del_list()

    def read_list(self):
        """
        Чтение списка из файла
        """
        list_file = input('Введите имя файла, который хотите открыть: ')
        if list_file == '00':
            exit(0)
        try:
            lst = open(f'{list_file}', 'rb')
            self.db += pickle.load(lst)
            lst.close()
        except FileNotFoundError:
            print(f'Файл {list_file} не найден.')
            Container().read_list()

    def write_list(self):
        """
        Запись списка в файл
        """
        list_file = input('Введите имя для сохраняемого списка: ')
        if list_file == '00':
            print('Выберите другои имя фвйла.')
            Container().write_list()
        else:
            l_file = open(f'{list_file}', 'wb')
            pickle.dump(self.db, l_file, 2)
            print(f'\nФайл {list_file} сохранен')
            sleep(2)

    def clear_list(self):
        """
        Очистка списка
        """
        q = input('Вы уверены, что хотите очистить список? (Н/д): ').lower()
        if q == 'д' or q == 'y' or q == 'да' or q == 'yes':
            self.db.clear()
            print('Список очищен.')
            sleep(2)
        else:
            print('Отмена.')
            sleep(2)


if __name__ == '__main__':
    pass
