
class economie:
    "Creer une class employe"

    def __init__(self):
        self.name=''
        self.secondname='' 
        self.place= ''
        
    def edit(self):
        self.name=input("name: ")
        self.secondname=input("second name: ")
        self.place=input("num place: ")
    
        
    def __str__(self):
        
        return f"{self.name},{self.secondname},{self.place}"
    
