from DataPersone import DataPersone

class DluyaNewPersone(DataPersone):

        def __init__(self):
            self.set_data()
        
        def set_data(self):
            DataPersone.set_data(self)
            self.staj = input("Стаж работы:")
            self.coins = input("Заработная плата:")
        
        def display_data(self):
            print(self.FIO, self.doljnost, self.staj, self.coins)
        
