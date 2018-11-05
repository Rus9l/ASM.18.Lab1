class book():
    
    def __init__(self):  
        self.author = '' 
        self.name = ''
        self.year = '' 
           
    def input(self):
        self.author = input('Введите автора ')        
        self.name = input('Введите название ')    
        self.year = input('Введите год ')       
        
    def print(self):
        print('''
автор: {0}
название: {1}
год: {2}
'''.format(self.author,self.name,self.year))
