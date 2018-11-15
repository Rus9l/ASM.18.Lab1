from container1 import ant_colony

a = ant_colony()

menu = {
    1: ('1: Добавить рабочего муравья', a.add_ant),
    2: ('2: Добавить солдата', a.add_soldier),
    3: ('3: Вывести весь список', a.print_colony),
    4: ('4: Импорт колонии в файл', a.import_to_file),
    5: ('5: Экспорт колонии из файла', a.export_from_file),
    6: ('6: Очистить список', a.delete_colony)
    }
	
def main():
    while True:

        for i in menu:
            print(menu[i][0])

        try:
            x = int(input())

            menu[x][1]()
        except KeyError as err:
            print(err, "Не является номером пункта меню")


if __name__ == '__main__':
    main()
	
	
	
