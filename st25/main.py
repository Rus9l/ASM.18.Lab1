if __name__ == '__main__':
    from database import Database
else:
    from .database import Database


def main():

    db = Database()

    while True:
        print('\n~~~~~База данных клиентов~~~~~')
        print('1 - Добавить клиента')
        print('2 - Добавить VIP-клиента')
        print('3 - Вывод базы на экран')
        print('4 - Сохранить базу в файл')
        print('5 - Загрузить базу из файла')
        print('0 - Выход')

        try:
            choice = int(input('Выберите действие: '))

            if choice == 0:
                print('Программа завершила работу. До скорой встречи!')
                break
            elif choice == 1:
                db.add_customer()
            elif choice == 2:
                db.add_vipcustomer()
            elif choice == 3:
                db.display_customers()
            elif choice == 4:
                db.save_to_file()
            elif choice == 5:
                db.load_from_file()
        except ValueError:
            print('\nТребуется ввести номер!')

if __name__ == '__main__':
	main()