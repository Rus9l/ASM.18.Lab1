if __name__ == '__main__':
    from book import book
    from bbook import bbook
else:
    from .book import book
    from .bbook import bbook

import pickle

FILENAME = '31.txt'

class Container():
    
    def __init__(self):
        self.container = []

    
    def add_book(self):
        bk = book()
        bk.input()
        self.container.append(bk)

    
    def add_bbook(self):
        bbk = bbook()
        bbk.input()
        self.container.append(bbk)

       
    def clear_container(self):
        answer = input('Вы действительно хотите все удалить?(да/нет)')
        if answer == 'да':
            self.container.clear()

    
    def show(self):
        for bk in self.container:
            bk.print()
                       
    
    def write_in_file(self):
        with open(FILENAME, 'wb') as file:
            pickle.dump(self.container, file)

    
    def read_from_file(self):
        with open(FILENAME, 'rb') as file:
            self.container = pickle.load(file)

        self.show()


        
