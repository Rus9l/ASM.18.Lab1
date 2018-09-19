import pickle
from .Specialist import Specialist
from .Head import Head


class Container:
    def __init__(self):
        self.workers = []

    def addworker(self):  #Добавить сотрудника
        self.workers.append(Specialist())
    def addhead(self):    #Добавить главу
        self.workers.append(Head())
    def clearcontainer(self): #Удаление
        self.workers.clear()
        print("Очищено!")
    def show(self):        #Вывод на всех элементов на экран
        if len(self.workers) == 0:
            print("Список пуст!")
        else:
            i=0
            for worker in self.workers:
                print(i, "_________________")
                worker.output()
                i+=1
    def infile(self):      #Запись в файл
        pickle.dump(self.workers,open('workers.pkl',"wb"))
        print ("Записано в файл.")
    def fromfile(self):    #Чтение из файла
        self.workers=pickle.load(open("workers.pkl","rb"))
        print("Список загружен из файла.")
    def edittarget(self):  #Редактировать элемент
        if len(self.workers) != 0:
            number=int(input("Введите номер сотрудника:"))
            if (number>=0) and (number<=len(self.workers)):
                self.workers[number].edit()
                print("Элемент успешно заменен!")
            else:
                print("Некорректный ввод")
        else:
            print("Список пуст!")
