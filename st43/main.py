#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 28 14:53:13 2018

@author: Shush_000
"""

from .otdel import Otdel


def main():
    work = Otdel()
    choice = input('''
    1 - добавить сотрудника
    2 - добавить директора
    3 - вывести список
    4 - записать в файл
    5 - загрузить из файла
    6 - очистить список
    7 - редактировать список
    ''')
    if choice == '1':
        work.add_worker()
    elif choice == '2':
        work.add_boss()
    elif choice == '3':
        work.output_spiska()
    elif choice == '4':
        work.write_file()
    elif choice == '5':
        work.read_file()
    elif choice == '6':
        work.clear()
    elif choice == '7':
        work.redact()
    main()


if __name__ == '__main__':
    main()
