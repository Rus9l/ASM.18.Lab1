# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:14:07 2018

@author: student
"""

from .animal import Animal

class Species(Animal):
    def __init__(self):
        super().__init__()
        self.breed = None
        self.masloradiatory = None

    @property
    def input(self):
        super().input
        self.breed = input('Введите породу животного: ')
        self.generations = input('Введите количество предков в родословной: ')

    @property
    def print(self):
        print('''Кличка: {0} Вид: {1} Породa: {2} Количество предков: {3}'''
   .format(self.name,
           self.view,
           self.breed,
           self.generations ))
    
        
a = Species()


