from ant import ant


class soldier(ant):
    def __init__(self):
        super().__init__()
        print('Введите цвет:')
        self.ant_colour = input()
		
        print('Наличие крыльев есть/нет:')
        self.ant_wings = input ()

    def print_element(self):
        super().print_element()
        print("Цвет:", self.ant_colour)
        print("Крылья:", self.ant_wings)