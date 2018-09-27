from .MobilePhone import MobilePhone
from .SmartPhone import SmartPhone
import pickle

class Shop:
    
    shop = []
    
    def __init__(self):
        pass
        
    def insert_MobilePhone(self):
        mobile_phone = MobilePhone()
        self.shop.append(mobile_phone)
        print("Мобильный телефон добавлен!")

    def insert_SmartPhone(self):
        smart_phone = SmartPhone()
        self.shop.append(smart_phone)
        print("Смартфон добавлен!")

    def edit_phone(self):
        if self.shop:
            self.display_shop()
            k = int(input("Введите номер телефона для редактирования:"))
            if k > len(self.shop):
                print("Число больше допустимого!")
            else:
                self.shop[k-1].set_data()
        else:
            print("Телефона нет в магазине!") 

    def delete_phone(self):
        if self.shop:
            self.display_shop()
            k = int(input("Введите номер телефона:"))
            if k > len(self.shop):
                print("Число больше допустимого!")
            else:   
                self.shop.pop(k-1)
                print("Телефон номер ", k, " удален!")
        else:
            print("Телефона нет в магазине!")
        
    def display_shop(self):
        if not self.shop:
            print("Телефона нет в магазине!")
        else:    
            for i in range (0, len(self.shop)):
                print("Телефон номер ", i+1)
                self.shop[i].display_data()

    def read_from_file(self):
        try:
            file = open('mobile_phone_shop.dat', 'rb')
            self.shop = pickle.load(file)    
            print("Выполнено!")
            file.close()
        except FileNotFoundError:
            print('\nФайл не существует')

    def write_to_file(self):
        file = open('mobile_phone_shop.dat', 'wb')
        pickle.dump(self.shop, file)        
        print("Выполнено!")
        file.close()    
            
    def clear_shop(self):
        self.shop.clear()
        print("Магазин пустой!")
        
