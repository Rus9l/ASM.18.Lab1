# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:27:26 2018

@author: Владимир
"""

class Truck:
    def __init__(self):
        self.input_data()
    
    def input_data(self):
        print("Please, insert data:")
        self.truck_model = input("Insert model of truck: ",)
        self.serial_number = input("Insert serial number of truck: ",)
        self.carrying = input("Insert carrying of truck (in kg's): ",)
        self.mileage = input("Insert mileage of truck (in km's): ",)
        
    def show_data(self):
        print("\nModel of truck: {}\nSerial number: {}\nCarrying: {}\nMileage: {}".format(self.truck_model,self.serial_number,self.carrying,self.mileage))
        
        
    