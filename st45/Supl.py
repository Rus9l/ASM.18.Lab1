#!/usr/bin/python3

from .Employe import Employe

class Supl(Employe):
    "Donnees supplemmentaires a la classe Employe"
    def __init__(self):
        self.serv=''
        self.codep=''
        Employe.__init__(self)

    def input(self):
        Employe.input(self)
        self.serv=input("Service: ")
        self.codep=input("Codep: ")
        

    def __str__(self):
        "Les donnees des employes entrees"
        
        return f"{self.name},{self.surname},{self.tel},{self.serv}, {self.codep}" 



    
        
