from .container import *

def main():
    c = Container()
    while True:
        choice = input('''
    1 - Add guitar
    2 - Add coolguitar
    3 - edit guitar
    4 - delete guitar
    5 - clear all
    6 - write in the file
    7 - read from the file
    8 - show the list
    ''')
        
        if choice == '1':
            c.add_guitar()
        elif choice == '2':
            c.add_coolguitar()
        elif choice == '3':
            c.edit()
        elif choice == '4':
            c.delete()
        elif choice == '5':
            c.clear_container()
        elif choice == '6':
            c.write()
        elif choice == '7':
            c.read()
        elif choice == '8':
            c.show()

    
if __name__ == '__main__':
    main()
