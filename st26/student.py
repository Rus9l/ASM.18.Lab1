# -*- coding: utf-8 -*-

class StudentCl:

    def __init__(self):
        self.input_student()

    def __str__(self):
        return f'[Студент][{self.name}, {self.age}, {self.number}]'

    def input_student(self):
        self.name = input('ФИО: ')
        self.age = input('Возраст: ')
        self.number = input('Телефон: ')

    def edit(self):
        self.input_student()


if __name__ == '__main__':
    pass
