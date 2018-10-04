# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:14:06 2018

@author: student
"""

from .container import Container



def main():
    
    while True:
        option = input('''
    1 - Добавить в картатеку новое животное
    2 - Добавить в картатеку новое породистое животное
    3 - Редактировать ячейку животного
    4 - Удалить выбранное животное
    5 - Удалить всю картотеку
    6 - Записать в файл картотеку
    7 - Считать из файла картотеку животных
    8 - Вывести картотеку животных
    9 - Выход из программы
   10 - О программе
   
    Ваш выбор: ''')
        print('''
              ''')
        
        if option == '1':
            a.AddAnimal
        elif option == '2':
            a.AddSpecies
        elif option == '3':
            a.EditAnimal
        elif option == '4':
            a.DeleteAnimal
        elif option == '5':
            a.ClearContainer
        elif option == '6':
            a.WriteFile
        elif option == '7':
            a.ReadFile
        elif option == '8':
            a.ShowContainer
        elif option == '9':
            break
        elif option == '10':
            a.Info
        else:
            print('Нет такого пункта меню')

a = Container()

if __name__ == '__main__':
	main()