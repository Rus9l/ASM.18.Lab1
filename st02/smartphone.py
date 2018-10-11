# -*- coding: utf-8 -*-
from device import Device


class Smartphone(Device):
    
    def __init__(self):
        super().read_input()
        self.read_input()


    def read_input(self):
        self.os = input('Операционная система: ')

    
    def display(self):
        super().display()
        print('- Операционная система: ', self.os)