class Specialist:
    def __init__(self):
        self.edit()

    def edit(self):
        self.fname = input("Введите имя:")
        self.lname = input("Введите фамилию")
        self.position = input("Введите должность")
        self.age = input("Введите возраст")
        self.ident = input("Введите ID")

    def output(self):
        print(" Имя:"+ self.fname, "\n Фамилия:"+self.lname, "\n Должн.:"+self.position, "\n Возраст:"+self.age, "\n ID:"+self.ident)
