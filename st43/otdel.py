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
        worker.vvod_w()
        self.ll.append(worker)

    def add_boss(self):
        boss = Boss()
        boss.vvod_b()
        self.ll.append(boss)

    def vivod_spiska(self):
        for Number, Object in enumerate(self.ll, start=1):
            print(Number, Object)

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
