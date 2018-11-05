
from book import book
from bbook import bbook

import pickle

FILENAME = '31.txt'

class Container():
    
    def __init__(self):
        self.container = []

    
    def add_book(self):
        book = book()
        book.input()
        self.container.append(book)

    
    def add_bbook(self):
        bbook = bbook()
        bbook.input()
        self.container.append(bbook)

       
    def clear_container(self):
        answer = input('Вы действительно хотите все удалить?(да/нет)')
        if answer == 'да':
            self.container.clear()

    
    def show(self):
        for book in self.container:
            book.print()
                       
    
    def write_in_file(self):
        with open(FILENAME, 'wb') as file:
            pickle.dump(self.container, file)

    
    def read_from_file(self):
        with open(FILENAME, 'rb') as file:
            self.container = pickle.load(file)

        self.show()


        
