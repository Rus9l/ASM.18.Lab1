class Student:
    def __init__(self):
        self.getInf()
        
    def getInf(self):
        print('Введите имя')
        self.firstName = input()
        print('Введите Фамилию')
        self.lastName = input()
        print('Введите возраст')
        self.age = input()
        
    def showInf(self):
        print('\nИмя: ' + self.firstName + '\nФамилия: ' + self.lastName + '\nВозраст: ' + self.age)
        