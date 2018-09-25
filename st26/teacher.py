# -*- coding: utf-8 -*-

from .student import StudentCl


class TeacherCl(StudentCl):

    def __init__(self):
        self.tch = None

    def read_from_console(self):
        """
        Функция чтения с консоли
        """
        self.tchr = input('Кафедра: ')

    def print_to_console(self):
        """
        Функция вывода в консоль
        """
        print(f'Кафедра: {self.tchr}')


if __name__ == '__main__':
    tch = TeacherCl()
    tch.read_from_console
    tch.print_to_console
