
from economie import economie
from business import business
import pickle


class Contener:

    def __init__(self):
        self.passager=[]
        
        
    def editE(self):
        eco = economie()
        eco.edit()
        self.passager.append(eco)
       

    def editB(self):
        bus = business()
        bus.edit()
        self.passager.append(bus)
            
    def ShowPas(self):
        if len(self.passager)==0:
            print('нет пассажера')
        
        for i in range(len(self.passager)):
            print(self.passager[i])
                         
    def write(self):        

        with open('Passagers','wb') as file:
            pickle.dump(self.passager,file)
            
        print('файл сохранен')
              

    def read(self):
        
        with open('Passagers','rb') as file:
            self.passager=pickle.load(file)
                
        self.ShowPas()

        
    def clear(self):
        self.passager.clear()
        print('Удалено')
    
        
    
