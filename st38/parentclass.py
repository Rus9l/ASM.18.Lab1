class Vehicle:
    
    def __init__(self):
        self.set()
        
    def set(self):
        print('Name:')
        self.name=input()
        print('Color:')
        self.color=input()
        print('Tires:')
        self.tires=input()
        
    def get(self):
             print(self.name)
             print(self.color)
             print(self.tires)
     
    
    

"""if __name__ == "__main__":
    car = Vehicle()
    car.get()"""
    

