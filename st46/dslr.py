"""@author: Рахиль Жаманкин"""

class DSLR():
    def __init__(self):
        self.model = ''
        self.year = ''
        self.price = ''     

    def __str__(self):
        return f'Камера. {self.model}, {self.year}, {self.price}'

    def input_d(self):
        self.model = input("Имя модели: ")
        self.year = input("Год: ")
        self.price = input("Цена: ")
  
    def edit(self):
        self.input_d()
