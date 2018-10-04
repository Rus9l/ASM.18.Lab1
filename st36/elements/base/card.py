from elements import base


class Card:

    def __init__(self, name=base.CARD_DEFAULT_NAME, surname=base.CARD_DEFAULT_SURNAME):
        self.name = name
        self.surname = surname

    def show_name(self):
        print ('Name: {}'.format(self.name))

    def show_surname(self):
        print ('Surname: {}'.format(self.surname))

    def set_name(self, name=''):
        self.name = name if name else input('Enter a name: ')

    def set_surname(self, surname=''):
        self.surname = surname if surname else input('Enter a surname: ')

    def __exec_by_var__(self, type='set'):
        for var in [el for el in dir(self) if not callable(getattr(self, el)) and not el.startswith("__")]:
            getattr(self, '{}_{}'.format(type, var))()

    def set(self):
        self.__exec_by_var__('set')
        return self

    @staticmethod
    def print_quotes(symbol=base.SHOW_QUOTES_FORMAT_DEFAULT, number=base.SHOW_QUOTES_NUMBER_DEFAULT):
        print (''.join([symbol for _ in range(number)]))

    def show(self):
        self.print_quotes(number=30)
        print ('Type: {}'.format(self.__class__.__name__))
        self.__exec_by_var__('show')
