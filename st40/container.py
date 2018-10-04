# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:14:09 2018

@author: student
"""

from .species import Species
from .animal import Animal
import pickle

FILENAME = 'shkurenkov40.txt'
class Container():
   
    def __init__(self):
        self.container = []
       
        
    @property
    def AddAnimal(self):
        animal = Animal()
        animal.input
        self.container.append(animal)
       

    @property
    def AddSpecies(self):
        animal = Species()
        animal.input
        self.container.append(animal)
        

    @property
    def  EditAnimal(self):
        if len(self.container) == 0:
                                     print("Список животных пуст.")
                                     return
        i=0
        for animal in self.container:
            i=i+1
            print('Животное под номером:',i,end=' - '),
            animal.print
        AnimalNum = int(input('Введите номер редактируемого животного в списке: '))
        AnimalNum=AnimalNum-1
        if AnimalNum < len(self.container) and AnimalNum > -1:
                                                           self.container[AnimalNum].input
        else:
            print("Ошибка при вводе значения")
            
    @property
    def DeleteAnimal(self):
        if len(self.container) == 0:
                                     print("Список животных пуст.")
                                     return
        i=0
        for animal in self.container:
            i=i+1
            print('Животное под номером:',i,end=' - '),
            animal.print
        AnimalNum = int(input('Введите номер удаляемого животного в списке: '))
        AnimalNum=AnimalNum-1
        if AnimalNum < len(self.container) and AnimalNum > -1:
            self.container.pop(AnimalNum)
            print("Животное удалено")  
        else:
            print("Ошибка при вводе значения")    
        

    @property
    def ClearContainer(self):
        ans = input('Вы действительно хотите все удалить?(да/нет): ')
        if ans == 'да':
            self.container.clear()
            print("Список животных очищен.")
        elif ans == 'нет':
            self.container.clear()
            print("Список животных не очищен.")
        else:
            print("Ошибка при вводе значения")

    @property
    def ShowContainer(self):
         if len(self.container) == 0:
                                     print("Список животных пуст.")
                                     return
         print("Общее число животных: ",len(self.container))
         for animal in self.container:
                                         animal.print
                
                       
    @property
    def WriteFile(self):
        if len(self.container) == 0:
                                     print("Список животных пуст.")
                                     return
        with open(FILENAME, 'wb') as file:
            pickle.dump(self.container, file)
            print("Список животных записан в файл: ", FILENAME)

    @property
    def ReadFile(self):
        with open(FILENAME, 'rb') as file:
            self.container += pickle.load(file)
            print("Список животных считан из файл: ", FILENAME)
    @property
    def Info(self):
            print('''
Программу написал
студент группы АСМ-1804
Шкуренков Виктор

задание взято с:
https://classroom.google.com/u/1/w/MTYzMDc2ODkwODBa/t/all
''')

a =  Container()
                       
            
        
