class Book(): #класс книги
    def __init__(self): #определение метода для класса, выполняется сразу после
                        #создания экзепляра класса 
        self.author = None #self-текущий экзепляр класса
        self.name = None
        self.year = None

    @property           #свойство
    def input(self):
        self.author = input('Введите автора ')         #ввод автора
        self.name = input('Введите название ')     #ввод названия
        self.year = input('Введите год ')       #ввод года
        
    @property
    def print(self):
        print
        ('''
автор: {0}
название: {1}
год: {2}
'''.format(self.author,
            self.name,
            self.year
            )
         )


