from .parentclass import Vehicle

class Airlane(Vehicle):
    
    def __init(self):
        self.set()
        
    def set(self):
        super().set()
        print('Wings:')
        self.wings=input()
        
    def get(self):
            super().get()
            print(self.wings)
    
    

