import pickle
if __name__ == '__main__':
    from customer import Customer
    from vip_customer import Customer
else:
    from .customer import Customer
    from .vip_customer import VipCustomer


class Database:

    def __init__(self):
        self.base = []

    def add_customer(self):
        print('\n~~~~~Добавление нового клиента~~~~~')
        customer = Customer()
        customer.read_data_from_concole()
        self.base.append(customer)

    def add_vipcustomer(self):
        print('\n~~~~~Добавление нового VIP-клиента~~~~~')
        vipcustomer = VipCustomer()
        vipcustomer.read_data_from_concole()
        self.base.append(vipcustomer)

    def display_customers(self):
        if len(self.base) == 0:
            print('База клиентов пуста')
        else:
            for i, customer in enumerate(self.base, start=1):
                print(f'\nКлиент №{i}')
                print('--------------------')
                print(customer)

    def load_from_file(self):
        try:
            with open('base.pickle', 'rb') as f:
                self.base = pickle.load(f)
                print('База клиентов загружена')

        except FileNotFoundError:
            print('\nFile does not exist')

    def save_to_file(self):
        filename = 'base.pickle'
        with open(filename, 'wb') as f:
            pickle.dump(self.base, f)
            print(f'База клиентов сохранена в файл {filename}')

    # def delete_customer(self):
    #     self.display_customers()
    #     while True:
    #         try:
    #             index = int(input('Введите номер клиента, которого хотите удалить: '))
    #             break
    #         except ValueError:
    #             print('Индекс должен быть целым неотрицательным числом! Попробуйте еще раз.')
    #         except IndexError:
    #             print(f'Номер должен быть в диапазоне от 0 до {len(self.base)} включительно.')
    #     del self.base[index]

    def clean_base(self):
        self.base.clear()
