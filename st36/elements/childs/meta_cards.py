from elements.base.card import Card
from elements import childs


class Student(Card):

    def __init__(self, uni=childs.DEFAULT_UNI_NAME, *args, **kwargs):
        self.uni = uni
        super().__init__(*args, **kwargs)

    def show_uni(self):
        print ('University: {}'.format(self.uni))

    def set_uni(self, uni=None):
        self.uni = uni if uni else input('Enter university: ')
