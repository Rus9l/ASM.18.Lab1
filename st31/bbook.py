from .book import *

class bbook(book):    #класс журнала
    def __init__(self): #определение метода для класса, выполняется сразу после
                        #создания экзепляра класса 
        b().__init__()
        self.publ = None  #self-текущий экзепляр класса
        self.num = None

    @property           #свойство
    def input(self):
        b().input
        self.publ = input('Введите издательство: ')    #издательство
        self.num = input('Введите номер: ')  #номер

    @property
    def print(self):
        print('''
автор: {0}
название: {1}
год: {2}
издательство: {3}
номер: {4}
'''.format(self.author,
            self.name,
            self.year,
            self.publ,
            self.num
            )
              )
    
        
a = bbook()
