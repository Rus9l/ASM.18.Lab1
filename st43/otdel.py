#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 28 11:23:12 2018

@author: Shush_000
"""

# "Pickling" - процесс преобразования объекта Python в поток байтов

import pickle
from .worker import Worker
from .boss import Boss


class Otdel:

    ll = []

    def add_worker(self):
        worker = Worker()
        worker.input_w()
        self.ll.append(worker)

    def add_boss(self):
        boss = Boss()
        boss.input_b()
        self.ll.append(boss)

    def output_spiska(self):
        for Number, Object in enumerate(self.ll, start=1):
            print(Number, Object)

    def redact(self):
        self.output_spiska()
        num = input('Введите номер объекта: ')
        """
        В модуль boss и worker добавлен метод edit, который вызывает
        метод ввода в соответствующем модуле.
        Т.к. в список записывается объект класса, достаточно вызвать метод
        edit к выбранному объекту из списка.
        int(num) - 1 т.к. список нумеруется с 0, соответственно 1 человек в
        выводе списка будет иметь 0 позицию в самом списке.
        """
        self.ll[int(num) - 1].edit()
        print('Редактировано')

    def write_file(self):
        file = open("spisok.dat", "wb")
        pickle.dump(self.ll, file)
        file.close()
        print("Записано")

    def read_file(self):
        file = open("spisok.dat", "rb")
        self.ll += pickle.load(file)
        file.close()
        print("Прочитано")

    def clear(self):
        self.ll.clear()
        print("Удалено")


if __name__ == '__main__':
    pass
