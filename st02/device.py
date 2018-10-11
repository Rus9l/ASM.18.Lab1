class Device:
    
    def __init__(self):
        self.read_input()


    def read_input(self):
        self.vendor = input('Производитель устройства: ')
        self.model = input('Модель: ')


    def display(self):
        print('- Производитель: ', self.vendor)
        print('- Модель: ', self.model)

