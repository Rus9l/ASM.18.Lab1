class Student:
    def write(self):
        self.name=input("Имя: ")
        self.age=input("Возраст: ")
        self.year=input("Курс: ")
        self.payment=input("Тип оплаты: ")

    def __str__(self):
        return 'Студент:\n Имя: %s\n Возраст: %s\n Курс: %s\n Тип: %s\n' %(self.name, self.age, self.year, self.payment)
