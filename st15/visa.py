class visa:
    
    def __init__(self):
        self.read_input()
    
    
    def read_input(self):
        self.name = input('Имя: ')       
        self.lastname = input('Фамилия: ')
        self.age = input('Дата рождения: ')
   
    
    
    def display(self):
        print('Имя: ', self.name)
        print('Фамилия: ',self.lastname)
        print ('Дата рождения: ',self.age)