from .worker import *
class Boss(Worker):
        def __init__(self,name='name', age='age', otdel='otdel', position='position', experience='experience'):
                super().__init__(name, age, otdel, position)
                self.experience=input('Введите опыт работы: ')  
        def WritePerson(self):
                    print('Имя: ',self.name, 'Возраст:',self.age,'Отдел: ', self.otdel,'Должность: ', self.position,'Опыт работы: ', self.experience ) 
        def EditPerson(self):
                super().EditPerson()
                self.experience=input('Введите новый опыт работы: ')
