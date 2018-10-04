# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:54:35 2018

@author: Владимир
"""

import pickle
from .truck import Truck
from .truck_driver import Truck_driver

class Autopark:
    def __init__(self):
        self.list_of_autopark = []
    
    def add_empty_truck(self):
        self.list_of_autopark.append(Truck())
   
    def add_truck_with_driver(self):
        self.list_of_autopark.append(Truck_driver())
   
    def clear_all(self):
        self.list_of_autopark.clear()
        print("Autopark is cleared\n")
    
    def present_autopark(self):
        print("\nList of Autopark: \n")
        for i in self.list_of_autopark:
            print("Truck number {}".format(self.list_of_autopark.index(i)+1))
            i.show_data()
            print("\n")
        if len(self.list_of_autopark) == 0:
            print("Autopark is empty now\n")
            
    def select_from_file(self):
        with open('filename.txt', 'rb') as filename:
            self.list_of_autopark = pickle.load(filename)
            
    def insert_into_file(self):
         with open("filename.txt", 'wb') as filename:
            pickle.dump(self.list_of_autopark, filename)
            
    def delete_truck(self):
        if len(self.list_of_autopark) != 0:
            print("Select number of truck for delete: ")
            num_del = int(input())
            if (num_edt>0) and (num_del<len(self.list_of_autopark)+1):
            	self.list_of_autopark.pop(num_del-1)
            	print("Truck number {} is delete\n".format(num_del))
            else:
                print("Bad input")
        else:
                print("Autopark is empty now\n")
            
        

    def edit_truck(self):
        if len(self.list_of_autopark) != 0:   
            print("Select number of truck for edit information about: ")
            num_edt = int(input())
            if (num_edt>0) and (num_edt<len(self.list_of_autopark)+1):
	            truck = self.list_of_autopark[num_edt-1]
	            self.list_of_autopark.pop(num_edt-1)
	            truck.input_data()
	            self.list_of_autopark.insert(num_edt-1, truck)
            else:
                 print("Bad input")
        else:
                print("Autopark is empty now\n")
         
    def end_function(self):
        print("Deleting all and exit...")
        return 0
