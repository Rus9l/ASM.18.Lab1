from .Group import *
import os
group=Group()
MENU = [
        ["Добавить студента", group.AddStudent],
        ["Добавить старшекурсника", group.AddUndergraduate],
        ["Вывести список на экран", group.ShowList],
        ["Записать список в файл", group.WriteToFile],
        ["Считать список из файла", group.ReadFromFile],
        ["Очистить список", group.ClearList],
        ["Редактировать элемент", group.ChangeStudent],
        ["Удалить элемент списка", group.DeleteStudent],
        ["Выход"]
    ]
def main():
    print("------------------------------")
    for i, item in enumerate(MENU):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    opt = int(input("Ввод: "))
    if opt != 8:
        MENU[opt][1]()
        main()

if __name__ == "__main__":
    try:
        main()
    except:
        print("Неверный ввод")
