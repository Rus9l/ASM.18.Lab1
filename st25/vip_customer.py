from .customer import Customer


class VipCustomer(Customer):
    def __init__(self):
        super().__init__()
        self.card_number = ''
        self.amount_of_discount = 0

    def read_data_from_concole(self):
        super().read_data_from_concole()
        self.card_number = input('Номер карты:')
        while True:
            try:
                self.amount_of_discount = int(input('Скидка:'))
                if self.amount_of_discount < 0 or self.amount_of_discount > 100:
                    raise ValueError
                break
            except ValueError:
                print('Скидка должна быть целым неотрицательным числом в диапазоне от 0 до 100%! Попробуйте еще раз.')

    def __str__(self):
        return super().__str__() + f"Номер карты: {self.card_number}\nРазмер скидки: {self.amount_of_discount}\n"


if __name__ == '__main__':
    cus = VipCustomer()
    cus.read_data_from_concole()
    print(cus)