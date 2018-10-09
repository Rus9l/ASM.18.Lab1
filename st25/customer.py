class Customer:
    def __init__(self):
        self.name = ''
        self.age = 0


    def read_data_from_concole(self):
        self.name = input('Имя клиента:')
        while True:
            try:
                self.age = int(input('Возраст клиента:'))
                if self.age <= 0:
                    raise ValueError
                break
            except ValueError:
                print('Возраст должен быть целым неотрицательным числом! Попробуйте еще раз.')

    # строковое представление объекта
    def __str__(self):
        return f"Имя клиента: {self.name}\nВозраст клиента: {self.age}\n"


if __name__ == '__main__':
    print('привет')
    cus = Customer()
    cus.read_data_from_concole()
    print(cus)