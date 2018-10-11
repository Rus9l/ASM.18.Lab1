"""@author: Рахиль Жаманкин"""

from .dslr import DSLR

class SLR(DSLR):
    
    def __init__(self):
        self.lens=''
        self.flens=''
        DSLR.__init__(self)

    def input_s(self):
        DSLR.input_d(self)
        self.lens=input("Объектив: ")
        self.flens=input("Диафрагма: ")
        

    def __str__(self):
     
        
        return f'Камера. {self.model},{self.year},{self.price},{self.lens}, {self.flens}' 