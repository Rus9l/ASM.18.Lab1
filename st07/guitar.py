class Guitar():
    def __init__(self):
        self.manufacture = ''
        self.model= ''
        self.color = ''

    def input(self):
        self.manufacture = input('Made by: ')
        self.model = input('Model is: ')
        self.color = input('Color is: ')

    def print(self):
        print('''
        Manufacture: {0}
        Model: {1}
        Color: {2}
        '''.format(self.manufacture, self.model, self.color))


