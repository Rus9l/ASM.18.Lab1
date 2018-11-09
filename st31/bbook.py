if __name__ == '__main__':
    from book import book
else:
    from .book import book


class bbook(book):    
    def __init__(self): 
        book.__init__(self)
        self.publ = None  #self-текущий экзепляр класса
        self.num = None


    def input(self):
        book.input(self)
        self.publ = input('Введите издательство: ')    #издательство
        self.num = input('Введите номер: ')  #номер

   
    def print(self):
        print('''
автор: {0}
название: {1}
год: {2}
издательство: {3}
номер: {4}
'''.format(self.author,self.name, self.year,self.publ,self.num))
    
