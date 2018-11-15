import pickle
from .worker import *
from .boss import * 
class Team:
        
        def __init__(self):
               self.spisok=[]
        def Add_worker(self):
                worker=Worker()
                self.spisok.append(worker)
        def Add_boss(self):
                boss=Boss()
                self.spisok.append(boss)
        def Edit(self):
                edit=int(input('Введите номер изменяемой записи: '))
                self.spisok[edit].EditPerson()
        def Display(self):
                if len(self.spisok)==0:
                        print('\nСписок пуст')
                        return
                for i in self.spisok:
                    i.WritePerson()
        def Clear(self):
                self.spisok.clear()

        def Writefile(self):
            file = open("file.txt", "wb")
            pickle.dump(self.spisok, file)
            file.close()
            print("Записано")
        
        def Readfile(self):
            file = open("file.txt", "rb")
            self.spisok += pickle.load(file)
            file.close()
            print("Прочитано")
                

