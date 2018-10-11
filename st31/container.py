from .bbook import *
import pickle

FILENAME = '31.txt'

class Container():
    
    def __init__(self):
        self.container = []

    @property
    def add_book(self):
        book = book()
        book.input
        self.container.append(book)

    @property
    def add_bbook(self):
        book = bbook()
        book.input
        self.container.append(book)

    @property
    def edit(self):
        book_number = int(input('введите номер редактируемого издания в списке'))
        self.container[book_number].input

    @property
    def delete(self):
        book_number = int(input('введите номер удаляемого издания в списке'))
        self.container.pop(book_number)

    @property
    def clear_container(self):
        answer = input('Вы действительно хотите все удалить?(да/нет)')
        if answer == 'да':
            self.container.clear()

    @property
    def show(self):
        for book in self.container:
            book.print
                       
    @property
    def write_in_file(self):
        with open(FILENAME, 'wb') as file:
            pickle.dump(self.container, file)

    @property
    def read_from_file(self):
        with open(FILENAME, 'rb') as file:
            self.container += pickle.load(file)

a =  Container()
                       
            
        
