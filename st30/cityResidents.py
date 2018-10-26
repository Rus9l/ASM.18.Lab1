if __name__ == '__main__':
    from human import Human
    from worker import Worker
else:
    from .human import Human
    from .worker import Worker

import pickle 

class CityResidents:
      
    def __init__(self):
        self.__residents = []
    
    def add_human(self):
        self.__residents.append(Human())
        
    def add_worker(self):
        self.__residents.append(Worker())
        
    def print(self):
        print("There are", len(self.__residents), "residents:")
        i = 1
        for p in self.__residents:
            print("##################")
            print("№" + str(i))
            p.print()
            print("##################")
            i += 1
    
    def __check_range(self, i):
        if i < 0 or i >= len(self.__residents):
            raise IndexError("Out of range")
                     
    def clear(self):
        self.__residents.clear()
        
    def edit(self):
        i = int(input("Index: "))
        self.__check_range(i - 1)
        self.__residents[i - 1].read() 
        
    def delete(self):
        i = int(input("Index: "))
        self.__check_range(i - 1)
        del self.__residents[i - 1]
    
    def save(self):
        with open("base", "wb") as f:
            pickle.dump(self.__residents, f)
            
    def load(self):
        with open("base", "rb") as f:
            self.__residents = pickle.load(f)
        