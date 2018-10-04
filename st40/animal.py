# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:14:07 2018

@author: student
"""

class Animal():
    def __init__(self):
        self.name = None
        self.view = None
       
    @property
    def input(self):
        self.name = input('Введите кличку животного: ')
        self.view = input('Введите вид животного:')
       
        
    @property
    def print(self):
        print('''Кличка: {0} Вид: {1} '''.format(self.name, self.view))