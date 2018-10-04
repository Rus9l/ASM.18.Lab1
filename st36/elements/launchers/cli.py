from elements.base.card import Card
from elements.childs.meta_cards import Student
from elements.containers.group import Group
from elements.launchers import pipeline


class Main:

    def __init__(self):
        self.card_types = [Card, Student]
        self.container_types = [Group]
        self.realized = []
        self.base_menu = {
            '0': {
                'text': 'Quit',
                'step': self.exit,
                'args': None
            },
            '1': {
                'text': 'Start Menu',
                'step': self.start,
                'args': None
            }
        }
        self.start_menu = {
            '2': {
                'text': 'Create new container',
                'step': self.create,
                'args': None
            },
            '3': {
                'text': 'Work with proceeded',
                'step': self.keeped,
                'args': None
            },
        }
        self.start_menu.update(self.base_menu)

    def exit(self):
        pass

    def add_by_class(self, class_):
        self.realized.append(class_())
        print ('Added successfully')
        self.start()

    def create(self):
        menu = {
            str(i+2): {
                'text': el,
                'step': self.add_by_class,
                'args': [el],
            } for i, el in enumerate(self.container_types)
        }
        self.execute_menu(menu)

    def event_for_obj(self, obj, func):
        menu = {
            str(i + 2): {
                'text': card_type.__name__,
                'step': pipeline,
                'args': [[getattr(obj, func), card_type], [self.start]],
            } for i, card_type in enumerate(self.card_types)
        }
        self.execute_menu(menu)

    def work_obj(self, obj):
        funcs = [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith("__")]
        menu = {
            str(i+2): {
                'text': func,
                'step': pipeline if func != 'add_by_class' else self.event_for_obj,
                'args': [[getattr(obj, func)], [self.start]] if func != 'add_by_class' else [obj, 'add_by_class'],
            } for i, func in enumerate(funcs)
        }
        self.execute_menu(menu)

    def keeped(self):
        menu = {
            str(i+2): {
                'text': el,
                'step': self.work_obj,
                'args': [el],
            } for i, el in enumerate(self.realized)
        }
        self.execute_menu(menu)

    def execute_menu(self, menu):
        if not set(menu.keys()) & set(self.base_menu.keys()):
            menu.update(self.base_menu)

        for k, v in menu.items():
            print ('[{}] - {}'.format(k, v['text']))

        cmd = input('Enter command number: ')
        if cmd in menu.keys():
            tmp = menu[cmd]
            if tmp['args']:
                tmp['step'](*tmp['args'])
            else:
                tmp['step']()
        else:
            print ('ERROR! No such command')
            self.start()

    def start(self):
        self.execute_menu(self.start_menu)

    def launch(self):
        self.start()
