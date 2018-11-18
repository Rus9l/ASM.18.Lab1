class Sensor:

    def __init__(self):
        self.set_data()

    def set_data(self):
        self.name = input('Введите название датчика: ')
        self.type = input('Введите тип датчика: ')
        self.output_signal = input('Введите тип выходного сигнала: ')

    def print_data(self):
        print(self.name, self.type, self.output_signal)
