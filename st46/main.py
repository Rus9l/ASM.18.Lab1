"""@author: Рахиль Жаманкин"""
from .container import Container
    
camera = Container()

menu = [
        ["Добавить DSLR", camera.add_dslr],
        ["Добавить SLR", camera.add_slr],
        ["Показать список камер", camera.show],
        ["Записать в файл", camera.save],
        ["Загрузить список из файла", camera.open],
        ["Очистить список", camera.clear],
        ["Выход"]
    ]

def main():
    i = 0
    for item in menu:
        print("{0:2}. {1}".format(i, item[0]))
        i += 1
    num = int(input("Введите пункт меню: "))
    if num != 6:
        menu[num][1]()
        main()

if __name__ == '__main__':
	main()