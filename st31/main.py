if __name__ == '__main__':
    from container import Container
else:
    from .container import Container

cont = Container()

def main():
    menu={'1':('добавить книгу',cont.add_book),
          '2':('добавить журнал',cont.add_bbook),
          '3':('вывести список',cont.show),
          '4':('записать в файл',cont.write_in_file),
          '5':('считать с файла',cont.read_from_file ),
          '6':('удалить все',cont.clear_container),
          '0':('выход',exit)
        } 

    for i in menu.keys():
        print(i,'',menu[i][0])

    while True:
        choice=input('Ваш выбор: ')
        if choice=='0':
            break
        menu.get(choice)[1]()


if __name__ == '__main__':
    main()
