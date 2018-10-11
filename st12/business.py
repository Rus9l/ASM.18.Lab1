
from economie import economie

class business(economie):

    def __init__(self):
        self.food=''
        economie.__init__(self)

    def edit(self):
        economie.edit(self)
        self.food=input("Food: ")
        

    def __str__(self):
        
        return f"{self.name},{self.secondname},{self.place},{self.food}" 



    
        
