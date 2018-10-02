# -*- coding: utf-8 -*-

from .student import StudentCl


class TeacherCl(StudentCl):

    def __init__(self):
        super().__init__()
        self.input_teacher()

    def __str__(self):
        return f'[Преподаватель][{self.name}, {self.age}, {self.number}, {self.tch}]'

    def input_teacher(self):
        self.tch = input('Кафедра: ')

    def edit(self):
        self.input_student()
        self.input_teacher()


if __name__ == '__main__':
    pass
