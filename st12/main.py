
from Contener import Contener

    
def main():
    Pas = Contener()
    
    menu={'1':('экономичный класс',Pas.editE),
          '2':('бизнес класс',Pas.editB),
          '3':('Список пассажеров',Pas.ShowPas),
          '4':('Добавить в файле',Pas.write),
          '5':('Читать файл',Pas.read),
          '6':('Удалить пассажеров',Pas.clear),
          '7':('Exit',exit)
        } 

    for num in menu.keys():
        print(num,'',menu[num][0])

    while True:
        choix=input('Ваш выбор: ')
        if choix=='7':
            break
        menu.get(choix)[1]()
    
            
            
            
if __name__=='__main__':
    main()

