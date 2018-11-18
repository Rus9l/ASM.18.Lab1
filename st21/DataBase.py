import pickle

from .sensor import Sensor
from .specs import Specs

class SensorDB:

    def __init__(self):
        self.__db = []
        self.__filename = 'st20/data'

    def add_sensor(self):
        sensor = Sensor()
        self.__db.append(sensor)
        print('Датчик добавлен в базу данных')

    def add_sensor_specs(self):
        specs = Specs()
        self.__db.append(specs)
        print('Исполнение датчика добавлено')

    def edit_sensor_data(self):
        if self.__db:
            print('Количество датчиков в базе: {}'.format(len(self.__db)))

            try:
                sensor_index = int(input('Введите номер датчика: '))
                self.__db.set_data()
                print('Информация по датчику №' + sensor_index + ' изменена')

            except Exception:
                print('Произошла ошибка!')

        else:
            print('База данных пуста!')

    def print_sensor_list(self):
        if not self.__db:
            print('База данных пуста!')
            return

        for item in self.__db:
            item.print_data()

    def save_to_file(self):
        with open(self.__filename, 'wb') as f:
            pickle.dump(self.__db, f, -1)
            print('Сохранение прошло успешно')


    def load_from_file(self):
        try:
            with open(self.__filename, 'rb') as f:
                self.__db = pickle.load(f)

            print('Информация загружена')
        
        except FileNotFoundError:
            print('Файл не найден!')


    def delete_sensor(self):
        if self.__db:
            print('Количество датчиков в базе: {}'.format(len(self.__db)))

            try:
                sensor_index = int(input('Введите номер датчика: '))
                self.__db.set_data()
                print('Информация по датчику №' + sensor_index + ' удалена')

            except Exception:
                print('Произошла ошибка!')

        else:
            print('База данных пуста!')


    def clear_db(self):
        self.__db = []
