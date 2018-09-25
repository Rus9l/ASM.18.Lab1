# -*- coding: utf-8 -*-


class StudentCl:

    def __init__(self):
        self.age = None
        self.group = None

    def read_from_console(self):
        """
        Функция чтения с консоли
        """
        self.age = input('Возраст: ')
        self.group = input('Группа: ')

    def print_to_console(self):
        """
        Функция вывода в консоль
        """
        print(f'Возраст: {self.age}')
        print(f'\nГруппа: {self.group}')


if __name__ == '__main__':
    st = StudentCl
    st.read_from_console
    st.print_to_console
