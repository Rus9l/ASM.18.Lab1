# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 09:31:45 2018

@author: Александр
"""
from .baseAcademicPlan import BaseAcademicPlan

class ExtendedAcademicPlan(BaseAcademicPlan):
    def __init__(self):
        # вызываем инициализацию родительского класса
        super().__init__()
        
        self._groupId = int
        self._purpose = str
        self.readExtendedProperties()
        super().printProperties()
        self.printProperties()
        
    @property
    def groupId(self):
        return self._groupId
    
    @property    
    def purpose(self):
        return self._purpose

    @groupId.setter
    def groupId(self, value):
        self._groupId = value
        
    @purpose.setter
    def purpose(self, value):
        self._purpose = value    
        
    def readExtendedProperties(self):
        try:
            self.groupId = int(input('Введите groupId учебного плана '))
            self.purpose = input('Введите цель ')
        except Exception as e:
            raise
            # вызвать выход из программы
            
    def printProperties(self):
        super().printProperties()
        print (
            "  5) id группы = " + str(self.groupId) +
            "\n 6) Цель - " + str(self.purpose) + "\n" 
        )