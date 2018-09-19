from .Specialist import Specialist


class Head(Specialist):
    def __init__(self):
        super().__init__()
        self.edit()
    def edit(self):
        super().edit()
        self.phone = input("Введите телефон гл. отдела:")
        self.code = input("Введите спец. ID")
    def output(self):
        print(" Имя:"+ self.fname, "\n Фамилия:"+self.lname, "\n Должн.:"+self.position, "\n Возраст:"+self.age, "\n ID:"+self.ident, "\n Телефон:"+self.phone, "\n Спец. ID:"+self.code)
