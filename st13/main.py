from spisok import Spisok

spisok = Spisok()

menucompany = {"1": ("Внести руководителя отдела", spisok.insert_DataPersone),
               "2": ("Внести новго сотрудника", spisok.insert_DluyaNewPersone),
               "3": ("Изменить данные сотрудника", spisok.edit_personal),
               "4": ("Удалить сотрудника из базы", spisok.delete_personal),
               "5": ("Вывести список сотрудников", spisok.display_spisok),
               "6": ("Звписать список сотрудников в файл", spisok.write_to_file),
               "7": ("Подгрузить список сотрудников из файла", spisok.read_from_file),
               "8": ("Очистить весь список", spisok.clear_spisok1),
               "9": ("Выйти из меню", "")
               }


def main():
            while True:
                for i in menucompany:
                    print(i,": ", menucompany[i][0])
                try: 
                            c=int(input("Введите номер пункта меню для начала работы приложения:"))        
                            if c <= len(menucompany):
                                if int(c) == 9:
                                    break
                                else:
                                    menucompany[str(c)][1]()
                            else:
                                print("Число не может быть больше 9")
                except ValueError:
                    print("Вы не ввели номер пункта меню")



if __name__ == "__main__":
        main()
            
        
