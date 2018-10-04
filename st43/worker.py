#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 28 10:03:50 2018

@author: Shush_000
"""

class Worker():
# метод вызывается всякий раз, когда вы создаете (или создаете экземпляр) объект
# на основе этого класса
# Слово self это способ описания любого объекта

    def __init__(self):
# атрибуты
        self.name = ''
        self.age = ''
        self.otdel = ''
        self.position = ''

    def __str__(self):
        return f'Сотрудник. {self.name}, {self.age}, {self.otdel}, {self.position}'

# методы
    def input_w(self):
        self.name = input("Имя сотрудника: ")
        self.age = input("Возраст сотрудника: ")
        self.otdel = input("Отдел сотрудника: ")
        self.position = input("Должность сотрудника: ")

    def edit(self):
        self.input_w()

    def output_w(self):
        print("Сотрудник: ", self.name)
        print("Возраст: ", self.age)
        print("Отдел: ", self.otdel)
        print("Должность: ", self.position)


if __name__ == '__main__':
    w = Worker()
    w.input_w()
    w.output_w()







