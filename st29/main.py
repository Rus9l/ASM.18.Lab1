from .shop import Shop

shop = Shop()

menu = {"1": ("Добавить мобильный телефон", shop.insert_MobilePhone),
        "2": ("Добавить смартфон", shop.insert_SmartPhone),
        "3": ("Изменить", shop.edit_phone),
        "4": ("Удалить", shop.delete_phone),
        "5": ("Показать телефоны", shop.display_shop),
        "6": ("Записать в файл", shop.write_to_file),
        "7": ("Считать из файла", shop.read_from_file),
        "8": ("Очистить", shop.clear_shop),
        "9": ("Выйти", "")
    }

def main():
    while True:
        for i in menu:
            print(i,": ", menu[i][0])
        try: 
            k=int(input("Введите номер команды:"))          
            if k <= len(menu):
               if int(k) == 9:
                   break
               else:
                   menu[str(k)][1]()
            else:
                print("Число больше допустимого!")
        except ValueError:
            print("Вы должны ввести число!")

if __name__ == "__main__":
    main()
            
        
