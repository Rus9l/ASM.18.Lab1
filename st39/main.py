# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:58:22 2018

@author: Александр
71"""
from .planList import PlanList

planList = PlanList()
MENU = [
        ["Добавить основной учебный план", planList.addBasePlan],
        ["Добавить расширенный учебный план", planList.addExtendedPlan],
        ["Вывести весь список на экран", planList.printElements],
        ["Очистить список", planList.eraseElements],
        ["Вывести список в файл", planList.printToFile],
        ["Загрузить список из файла", planList.downloadElementsFromFile],
        ["Редактировать план", planList.editPlan]
	]


def menu():
	print("------------------------------")
	for i, item in enumerate(MENU):
		print("{0:2}. {1}".format(i+1, item[0]))
	print("------------------------------")
	return int(input())

    
def main():
    try:
    	while True:
    		MENU[menu()-1][1]()
    except Exception as ex:
    	print(ex, "\nbye")

if __name__ == "__main__":
    main()
