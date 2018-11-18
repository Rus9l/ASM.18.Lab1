from .sensor import Sensor

class Specs(Sensor):

    def __init__(self):
        self.set_data()

    def set_data(self):
        Specs.set_data(self)
        self.case = input('Введите тип копуса: ')
        self.prim_transducer = input('Введите тип чувствительного элемента: ')

    def print_data(self):
        print(self.name, self.type, self.output_signal, self.case, self.prim_trancducer)
