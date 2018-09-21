from .base import Student
class Captain(Student):
    def __init__(self):
        self.getInf()
        
    def getInf(self):
        super().getInf()
        print('Введите почту')
        self.mail = input()
        print('Введите телефон')
        self.phone = input()
        
    def showInf(self):
        super().showInf()
        print('Почта: ' + self.mail + '\nТелефон: ' + self.phone)
        
        