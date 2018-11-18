from .DataBase import SensorDB

db = SensorDB()

MENU = [
    ('Добавить датчик', db.add_sensor),
    ('Добавить исполнение датчика', db.add_sensor_specs),
    ('Просмотреть всю базу датчиков', db.print_sensor_list),
    ('Изменить информацию по датчику', db.edit_sensor_data),
    ('Сохранить в файл', db.save_to_file),
    ('Загрузить из файла', db.load_from_file),
    ('Удалить датчик', db.delete_sensor),
    ('Очистить', db.clear_db)
]


def print_menu():
    print("***********************")
    for i, item in enumerate(MENU, start=1):
        print("{0} {1}".format(i, item[0]))
    print("***********************")


def main():
    print("***********************")

    while True:
        print_menu()

        try:
            user_choice = int(input('>> '))

            if user_choice == 0:
                break

            MENU[user_choice - 1][1]()
        
        except Exception:
            print("Произошла ошибка!")
