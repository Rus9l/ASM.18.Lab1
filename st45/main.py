#!/usr/bin/python3

from .Group import Group
G=Group()
    
def main():
    menu={'1':('ajout employe',G.AjoutE),
          '2':('ajout other data',G.AjoutS),
          '3':('print',G.Print),
          '4':('write in file',G.WriteFile),
          '5':('read file',G.ReadFile),
          '6':('delete liste',G.Delete),
          '7':('Exit',exit)
        } 

    for key in menu.keys():
        print(key,'',menu[key][0])

    while True:
        choix=input('what u would do: ')
        if choix=='7':
            break

        try:
            menu.get(choix)[1]()
        except:
            print('Enter number between 1 and 7')
            
            
            


if __name__=='__main__':
    main()

