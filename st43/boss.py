#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 28 11:06:30 2018

@author: Shush_000
"""

from .worker import Worker


class Boss(Worker):

    def __init__(self):
        # Необходимо вызвать метод инициализации родителя.
        # В Python 3.x это делается при помощи функции super()
        super().__init__()
        self.name = ''
        self.age = ''
        self.experience = ''

    def __str__(self):
        return f'Директор отдела. {self.name}, {self.age}, {self.experience}'

    def input_b(self):
        self.name = input("Имя директора отдела: ")
        self.age = input("Возраст директора отдела: ")
        self.experience = input("Стаж директора отдела: ")

    def edit(self):
        self.input_b()

    def output_b(self):
        print("Директор отдела: ", self.name)
        print("Возраст: ", self.age)
        print("Стаж: ", self.experience)


if __name__ == '__main__':
    b = Boss()
    b.input_b()
    b.output_b()
