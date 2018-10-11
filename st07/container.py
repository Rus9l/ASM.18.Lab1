from .coolguitar import *
import pickle

FILENAME = '28.txt'

class Container():
    
    def __init__(self):
        self.container = []

    def add_guitar(self):
        guitar = Guitar()
        guitar.input()
        self.container.append(guitar)

    def add_coolguitar(self):
        coolguitar = Coolguitar()
        coolguitar.input()
        self.container.append(coolguitar)

    def edit(self):
        guitar_number = int(input('Guitar you want to edit:'))
        self.container[guitar_number].input()

    def delete(self):
        guitar_number = int(input('Guitar you want to delete'))
        self.container.pop(guitar_number)


    def clear_container(self):
        self.container.clear()


    def show(self):
        for guitar in self.container:
            guitar.print()
                       
    def write(self):
        with open(FILENAME, 'wb') as file:
            pickle.dump(self.container, file)

    def read(self):
        with open(FILENAME, 'rb') as file:
            self.container += pickle.load(file)

a =  Container()
                       
            
        
