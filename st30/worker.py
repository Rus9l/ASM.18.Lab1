from human import Human

class Worker(Human):
    
    def __init__(self):
        self.read()
               
    def read(self):
        Human.read(self)
        self.__position = input("Position: ")
        self.__salary = int(input("Salary: "))
        
    def print(self):
        Human.print(self)
        print("Position: ", self.__position)
        print("Salary: ", self.__salary)