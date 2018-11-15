from .team import *
team=Team()
def main():
    choice = input('''
    1 - добавить сотрудника
    2 - добавить начальника
    3 - редактировать список
    4 - вывести список
    5 - записать в файл
    6 - загрузить из файла
    7 - очистить список

    ''')
    if choice == '1':
        team.Add_worker()
    elif choice == '2':
        team.Add_boss()
    elif choice == '3':
        team.Edit()
    elif choice == '4':
        team.Display()
    elif choice == '5':
        team.Writefile()
    elif choice == '6':
        team.Readfile()
    elif choice == '7':
        team.Clear()
    main()

