"""@author: Рахиль Жаманкин"""
from .container import Container
def main():
    camera = Container()
    choice = input('''
    1 - Добавить DSLR
    2 - Добавить SLR
    3 - Показать список камер
    4 - Сохранить в файл
    5 - Показать из файла
    6 - Очистить список
    ''')
    
    if choice == '1':
        camera.add_dslr()
    elif choice == '2':
        camera.add_slr()
    elif choice == '3':
        camera.show()
    elif choice == '4':
        camera.save()
    elif choice == '5':
        camera.open()
    elif choice == '6':
        camera.clear()
    
    main()
    
if __name__ == '__main__':
    main()