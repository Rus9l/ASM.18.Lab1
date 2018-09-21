import pickle
from .base import Student
from .derived import Captain

class Group:
    
    def __init__(self):
        self.group = []
        
    def addStudent(self):
        self.group.append(Student())  
        
    def addCaptain(self):
        self.group.append(Captain()) 
        
    def showStudent(self):
        print('\nВведите номер студента')
        index = int(input()) - 1
        if(len(self.group) > index):
            self.group[index].showInf()
        else:
            print('Студента с таким номером не существует')
            
    def showAllStudents(self):
        if (len(self.group) != 0):
            for curStudent in self.group:
                print('\nНомер: ' + str(self.group.index(curStudent) + 1))
                curStudent.showInf()
        else:
            print('В группе еще нет студентов')
            
    def deleteStudent(self):
        print('\nВведите номер')
        index = int(input()) - 1
        if(len(self.group) > index):
            self.group.remove(self.group[index])
            print('Студентов в группе: ' + str(len(self.group)))
        else:
            print('Студента с таким номером не существует')
            
    def deleteAllStudents(self):
        self.group = []             
            
    def editStudent(self):
        print('\nВведите номер')
        index = int(input()) - 1
        if(len(self.group) > index):
            self.group[index].getInf()
        else:
            print('Студента с таким номером не существует')
    
    def saveToFile(self):
        file = input('Введите имя файла\n')
        with open('st19/' + file, 'wb') as f:
            pickle.dump(self.group, f)   

    def addFromFile(self):
        file = input('Введите имя файла\n')
        try: 
            with open('st19/' + file, 'rb') as f:
                self.group.extend(pickle.load(f)) 
        except FileNotFoundError:
            print('Файл не найден')    
            
