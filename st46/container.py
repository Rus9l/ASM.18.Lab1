"""@author: Рахиль Жаманкин"""
import pickle
from .dslr import DSLR
from .slr import SLR

class Container:
    list = []
    
    def add_dslr(self):
        dslr = DSLR()
        dslr.input_d()
        self.list.append(dslr)
        
    def add_slr(self): 
        slr = SLR()
        slr.input_s()
        self.list.append(slr)
        
    def show(self):
        if len(self.list)==0:
            print('Лист пуст')
        
        for i in range(len(self.list)):
            print(i+1,self.list[i])        
    
    def save(self):
        with open('Camera','wb') as fich:
            pickle.dump(self.list,fich)   
        print('Успешно!')
    
    
    def open(self):
        with open('Camera','rb') as fich:
            self.list=pickle.load(fich)
        self.show()

    def clear(self):
        self.list.clear()
        print('Очищено!')

