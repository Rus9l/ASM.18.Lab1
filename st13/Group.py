import pickle 
from .Student import *
from .Undergraduate import *

class Group:
    def __init__(self):
        self.group=[]
        
    def AddStudent(self):
        student=Student()
        student.write()
        self.group.append(student)

    def AddUndergraduate(self):
        student=Undergraduate()
        student.write()
        self.group.append(student)
        
    def ShowList(self):
        if len(self.group)==0:
            print("Список пуст!")
        else:
            i = 0
            print("Список:")
            for x in self.group:
                print(i,x)
                i+=1
            
    def ClearList(self):
        self.group.clear()
        print("Список очищен!")

    def WriteToFile(self):
        pickle.dump(self.group, open('st07/file.dat', 'wb'))
        print("Запись в файл успешно выполнена!")

    def ReadFromFile(self):
        self.group=pickle.load(open('st07/file.dat', 'rb'))
        print("Чтение из файла успешно выполнено!")

    def ChangeStudent(self):
        if len(self.group)==0:
            print("Список пуст!")
            return
        n=int(input("Введите номер объекта:"))
        if n<=len(self.group)-1 and 0<=n:
            print("Успешный ввод!")
            self.group[n].write()
            print("Замена выполнена!")
        else:
            print("Некорректный ввод!")
            
    def DeleteStudent(self):
        if len(self.group)==0:
            print("Список пуст! ")
            return
        n=int(input("Введите номер объекта: "))
        if n<=len(self.group)-1 and 0<=n:
            print("Успешный ввод!")
            self.group.pop(n)
            print("Удаление выполнено! ") 
        else:
            print ("Некорректный ввод!")
