from .DataPersone import DataPersone
from .DluyaNewPersone import DluyaNewPersone
import pickle

class Spisok:
    
    spisok = []
    
    def __init__(self):
        pass
        
    def insert_DataPersone(self):
        New_persona = DataPersone()
        self.spisok.append(New_persona)
        print("Новый сотрудник добавлен!")

    def insert_DluyaNewPersone(self):
        New_boss = DluyaNewPersone()
        self.spisok.append(New_boss)
        print("Новый руководитель добавлен!")

    def edit_personal(self):
        if self.spisok:
            self.display_spisok()
            k = int(input("Введите id для редактирования сотрудника:"))
            if k > len(self.spisok):
                print("Число больше допустимого")
            else:
                self.spisok[k-1].set_data()
        else:
            print("Сотрудника нет в списке!") 

    def delete_personal(self):
        if self.spisok:
            self.display_spisok()
            k = int(input("Введите id сотрудника:"))
            if k > len(self.spisok):
                print("Число больше допустимого!")
            else:   
                self.spisok.pop(k-1)
                print("id сотрудника", k, " удален!")
        else:
            print("Список сотрудников пуст, вы никого не добавили!")
        
    def display_spisok(self):
        if not self.spisok:
            print("Список сотрудников пуст, вы никого не добавили!")
        else:    
            for i in range (0, len(self.spisok)):
                print("id сотрудника ", i+1)
                self.spisok[i].display_data()

    def read_from_file(self):
        try:
            file = open('Company_spisok_personal.dat', 'rb')
            self.spisok = pickle.load(file)    
            print("Выполнено!")
            file.close()
        except FileNotFoundError:
            print('\nФайл не существует')

    def write_to_file(self):
        file = open('Company_spisok_personal.dat', 'wb')
        pickle.dump(self.spisok, file)        
        print("Выполнено!")
        file.close()    
            
    def clear_spisok(self):
        self.spisok.clear()
        print("Список пуст!")
        
