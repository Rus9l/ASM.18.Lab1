import pickle

from .device import Device
from .smartphone import Smartphone


class Office:

    FILENAME = 'st01/test'

    def __init__(self):
        self.devices = []


    def add_device(self):
        b = Device()
        self.devices.append(b)


    def add_smartphone(self):
        m = Smartphone()
        self.devices.append(m)


    def print_list(self):
        if len(self.devices) == 0:
            print('Никого нет')
            return

        print('------------------------------')
        for p in self.devices:
            print('\t', p.__class__.__name__)
            p.display()
            print('------------------------------')


    def edit_list(self):
        if len(self.devices) == 0:
            print('Никого нет')
            return

        print('Число студентов: ', len(self.devices))

        try:    
            ind = int(input('Для редактирования введите индекс (0 вернуться назад): '))

            if ind == 0:
                return

            self.devices[ind - 1].read_input()
        except Exception as ex:
            print(ex)
            print('Ошибка!')


    def save_to_file(self):
        with open(self.FILENAME, 'wb') as f:
            pickle.dump(self.devices, f, -1)
            print('Список сохранен')


    def load_from_file(self):
        try:
            with open(self.FILENAME, 'rb') as f:
                self.devices = pickle.load(f)

            print('Загрузка списка выполнена')
        
        except FileNotFoundError:
            print('Файл не найден')


    def delete_from_list(self):
        if len(self.devices) == 0:
            print('Никого нет')
            return

        print('Число студентов: ', len(self.devices))
        
        try:
            ind = int(input('Индекс студента (0 вернуться назад): '))

            if ind == 0:
                return

            del self.devices[ind - 1]
            print('Удаление прошло успешно')
        
        except Exception as ex:
            print(ex)
            print('Ошибка!')

    
    def clear(self):
        self.devices = []