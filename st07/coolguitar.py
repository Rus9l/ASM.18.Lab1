from .guitar import *

class Coolguitar(Guitar):
    def __init__(self):
        super().__init__()
        self.autotune = ''
        self.strings = ''

    def input(self):
        super().input()
        self.autotune = input('Autotune?: ')
        self.strings = input('Amount of strings?')

    def print(self):
        print('''
        Manufacture: {0}
        Model: {1}
        Color: {2}
        Autotune: {3}
        Strings: {4}
        '''.format(self.manufacture,
                   self.model,
                   self.color,
                   self.autotune,
                   self.strings))
    
        
a = Coolguitar()
