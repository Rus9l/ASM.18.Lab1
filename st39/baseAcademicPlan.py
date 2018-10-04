# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:14:55 2018

@author: Александр
"""
global str

class BaseAcademicPlan:
    
    def __init__(self):
        self._id = int
        self._name = str
        self._yearBegin = int
        self._federalStudyStandardNumber = int
        self.readBaseProperties()
       
    @property
    def id(self):
        return self._id
    
    @property    
    def name(self):
        return self._name
    
    @property    
    def yearBegin(self):
        return self._yearBegin
    
    @property    
    def federalStudyStandardNumber(self):
        return self._federalStudyStandardNumber
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @name.setter
    def name(self, name):
        self._name = name
        
    @yearBegin.setter
    def yearBegin(self, value):
        self._yearBegin = int(value)
        
    @federalStudyStandardNumber.setter
    def federalStudyStandardNumber(self, value):
        self._federalStudyStandardNumber = int(value)      
    
    def readBaseProperties(self):
        try:
            self.id = int(input('Введите id учебного плана '))
            self.yearBegin = int(input('Введите год начала уч. плана '))
            self.name = input('Введите название учебного плана ')
            self.federalStudyStandardNumber = int(input('Введите номер ГОС '))
        except Exception as e:
            raise
            # вызвать выход из программы
            
    def printProperties(self):
        print (
            "Учебный план - \n 1) id = " + str(self.id) +
            "\n 2) Год начала - " + str(self.yearBegin) +
            "\n 3) Название - " + self.name +
            "\n 4) ГОС - " + str(self.federalStudyStandardNumber) + "\n"    
        )
        
    def editProperty(self, property, value):
        print (property)
        print (value)
        if type(getattr(self, property)) != int:
            setattr(self, property, value)
        else:    
            try:
                setattr(self, property, int(value))
            except Exception as e:
                print ('Ошибка в типе переменной')
            
            