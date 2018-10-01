from .visa import visa

class master(visa):
    
    def __init__(self):
        self.read_input()
    
    
    def read_input(self):
        super().read_input()
        self.pay=input('Нужен PayPass?: ')
   
    
    
    def display(self):
        super().display()
        print('Paypass: ', self.pay)