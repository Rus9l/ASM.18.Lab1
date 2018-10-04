# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:17:47 2018

@author: Александр
"""
from .extendedAcademicPlan import ExtendedAcademicPlan
from .baseAcademicPlan import BaseAcademicPlan
import pickle
import inspect

class PlanList:
    def __init__(self):
        self._elements = []
        
    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, plan):
        self._elements = self._elements.append(plan)
        
    def addBasePlan(self):
        baseAcademicPlan = BaseAcademicPlan()
        self._elements.append(baseAcademicPlan)
        
    def addExtendedPlan(self):
        self._elements.append(ExtendedAcademicPlan())
        
    def printElements(self):
        for i, element in enumerate(self.elements):
            print ('Учебный план № ' + str(i+1))
            element.printProperties()
            
    def eraseElements(self):
         self.elements.clear()
         
    def printToFile(self):
        try:
            with open('plans.data', 'wb') as filehandle:
                pickle.dump(self.elements, filehandle)
        except Exception as e:
            print("Ошибка при выгрузке в файл")
            print (e)
            # вызвать выход
            
    def downloadElementsFromFile(self):
        try:
            with open('plans.data', 'rb') as filehandle:
                self._elements = pickle.load(filehandle)
        except Exception as e:
            print("Ошибка при загрузки из файла")
            print (e)
            # вызвать выход
      
    def editPlan(self):
        enteredId = int(input('Введите id учебного плана, который хотите редактировать '))
        
        choiceProperty = 0
        for i, element in enumerate(self.elements):
            if element.id == enteredId:
                propertiesList = list(
                    inspect.getmembers(
                        element, predicate=inspect.getmembers
                    )[2][1].keys()
                )
                
                print ('\n Введите номер свойства которое необходимо отредактировать')
                for i, item in enumerate(propertiesList[1:]):
                   print ("{0:2}. {1}".format(i+1, item))
                
                # проверка на неправильный ввод
                choiceProperty = int(input())
                element.editProperty(
                    propertiesList[choiceProperty], 
                    input('Введите новое значение ')
                )
        if choiceProperty == 0:
            print ('Элемент с таким id не найден \n')
               
        