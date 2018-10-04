# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:27:06 2018

@author: Владимир
"""

from .autopark import Autopark

auto_park = Autopark()
def end_function():
    return
menu_list = [
                ["Add an empty truck", auto_park.add_empty_truck ],
                ["Add truck with driver", auto_park.add_truck_with_driver],
                ["Present autopark", auto_park.present_autopark ],
                ["Clear all autopark", auto_park.clear_all ],
                ["Delete one item", auto_park.delete_truck ],
                ["Edit item", auto_park.edit_truck ],
                ["Insert data into file", auto_park.insert_into_file ],
                ["Select data from file", auto_park.select_from_file ],
                ["Exit"  ],
            ]


def trucks_menu():
    print("-------------AUTOPARK--------------")
    for i, item in enumerate(menu_list):
        print("{0:2} - {1}".format(i+1, item[0]))
    print("----created by st32 <V.Sazonov>----\n")
    


def main():
    while True:
        trucks_menu()
        try:
            num_input = int(input())
            if num_input == 9:
                menu_list[3][1]()
                return
            menu_list[int(num_input) - 1][1]()
        except:
            print("Bad input, please, try again")


if __name__ == '__main__':
    main()
