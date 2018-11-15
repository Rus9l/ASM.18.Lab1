class Worker:
        def __init__(self, name='name', age='age', otdel='otdel', position='position'):
            name = input('Введите имя: ')
            age = int(input('Введите возраст: '))
            otdel = input('Введите отдел: ')
            position=input('Введите должность: ')     
            self.name = name
            self.age = age
            self.otdel = otdel
            self.position= position
        def WritePerson(self):
            print('Имя: ',self.name, 'Возраст:',self.age,'Город: ', self.otdel,'Должность: ', self.position )
        def EditPerson(self):
                self.name=input('Введите новое имя: ')
                self.age=input('Введите новый возраст: ')
                self.otdel=input('Введите новый отдел: ')
                self.position=input('Введите новую должность: ')
