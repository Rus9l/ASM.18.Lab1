class DataPersone:

        def __init__(self):
            self.set_data()
        
        def set_data(self):
            self.FIO = input("Введите ФИО:")
            self.doljnost = input("Введите отдел:")

        def display_data(self):
            print(self.FIO, self.doljnost)
    
        
