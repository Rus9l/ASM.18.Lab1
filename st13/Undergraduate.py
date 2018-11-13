from .Student import *
class Undergraduate(Student):
    def write(self):
        super().write()
        self.advisor=input("Научный руководитель: ")
        self.topic=input("Тема диплома: ")

    def __str__(self):
        return 'Старшекурсник:\n Имя: %s\n Возраст: %s\n Курс: %s\n Тип: %s\n Научный руководитель: %s\n Тема диплома: %s\n' %(self.name, self.age, self.year, self.payment, self.advisor, self.topic)
