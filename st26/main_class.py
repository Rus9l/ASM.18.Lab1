# -*- coding: utf-8 -*-


class MainClass:
    # name = ''
    # age = ''

    def __init__(self):
        self.name = None
        self.age = None

    def read_from_console(self):
        """
        Функция чтения с консоли
        """
        self.name = input('Введите имя: ')
        self.age = input('Введите возраст: ')

    def print_to_console(self):
        """
        Функция вывода в консоль
        """
        print(f'\nИмя: {self.name}')
        print(f'Возраст: {self.age}')


if __name__ == '__main__':
    mc = MainClass()
    mc.read_from_console
    mc.print_to_console
