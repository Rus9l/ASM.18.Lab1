from .container import *

def main():
    c = Container()
    while True:
        choice = input
        ('''
                        1 - добавить книгу
                        2 - добавить журнал
                        3 - редактировать выбранное издание
                        4 - удалить выбранное издание
                        5 - удалить все
                        6 - записать в файл
                        7 - считать с файла
                        8 - вывести список
        ''')
        
        if choice == '1':
                        c.add_book           #добавление книги
         
        elif choice == '2':
                        c.add_bbook      #добавление журнала
                        
        elif choice == '3':
                        c.edit              # редактирование
                        
        elif choice == '4':
                        c.delete            # удаление
                        
        elif choice == '5':
                        c.clear_container   # очистка
            
        elif choice == '6':
                        c.write_in_file     #сохранение в файл
            
        elif choice == '7':
                        c.read_from_file    #чтение из файла
            
        elif choice == '8':
                        c.show              #вывод



if __name__ == '__main__':
	main()
