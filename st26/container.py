# -*- coding: utf-8 -*-

from pickle import dump, load
from time import sleep
from os import system

from .teacher import TeacherCl
from .student import StudentCl


class Container:

    db = []

    def add_list_student(self):
        """
        Добавление студента в список.
        """
        print('Заполните данные:')
        std = StudentCl()
        self.db.append(std)
        system('cls')
        print(f'\nСтудент добавлен в список.')
        sleep(2)

    def add_list_teacher(self):
        """
        Добавление преподавателя в список.
        """
        print('Заполните данные:')
        tch = TeacherCl()
        self.db.append(tch)
        system('cls')
        print(f'\nПреподаватель добавлен в список.')
        sleep(2)

    def edit_list(self):
        """
        Редактирование записи в списке.
        """
        self.get_list()
        try:
            target = int(input('Введите номер редактируемого человека: '))
            self.db[target - 1].edit()
            print('Список отредактирован.')
            sleep(0.5)
        except IndexError:
            print('В списке нет такого номера.')
            sleep(0.5)
            self.edit_list()
        except ValueError:
            print('Необходимо ввести номер.')
            sleep(0.5)
            self.edit_list()

    def get_list(self):
        """
        Вывод списка.
        """
        if self.db == []:
            print('Список пуст.')
        else:
            for i, item in enumerate(self.db, start=1):
                print(f'{i}. {item}')
        sleep(2)

    def del_list(self):
        """
        Удаление записи из списка.
        """
        self.get_list()
        try:
            target = int(input('Введите номер удаляемого человека: '))
            self.db.pop(target)
        except IndexError:
            print('В списке нет такого номера.')
            sleep(0.5)
            self.del_list()
        except ValueError:
            print('Необходимо ввести номер.')
            sleep(0.5)
            self.del_list()

    def read_list(self):
        """
        Загрузка списка из файла.
        """
        list_file = input('Введите имя файла(00 для выхода): ')
        if list_file == '00':
            exit(0)
        try:
            with open(f'{list_file}', 'rb') as lst:
                self.db += load(lst)
        except FileNotFoundError:
            print(f'Файл {list_file} не найден.')
            self.read_list()

    def write_list(self):
        """
        Запись списка в файл.
        """
        list_file = input('Введите имя для сохраняемого списка: ')
        if list_file == '00':
            print('Выберите другои имя фвйла.')
            Container().write_list()
        else:
            with open(f'{list_file}', 'wb') as l_file:
                dump(self.db, l_file, 2)
            print(f'\nФайл {list_file} сохранен')
            sleep(2)

    def clear_list(self):
        """
        Очистка списка.
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
