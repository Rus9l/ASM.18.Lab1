import pickle

from Base import russia
from Bbase import norussia

class country():

    def __init__ (self):
        self.storage = []
    
    
    def add_food_r(self):
	    print ('Hello')
	    r=russia()
	    r.reading()
	    self.storage.append(r)
		
		
    def add_food(self):
        b = norussia()
        b.reading()
        self.storage.append(b)



    def print_storage(self):
        for i, food in enumerate(self.storage):
            print('\nFood #{}'.format(i))
            food.printing()	

    def write_to_file(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.storage, f)


    def load_from_file(self):
        try:
            with open('data.pickle', 'rb') as f:
                self.storage = pickle.load(f)
        
        except FileNotFoundError:
            print('\nFile does not exist')


    def delete_food_from_menu(self, index: int):
        del self.storage[index]
    
    
    def clean_storage(self):
        del self.storage[:]




if __name__ == '__main__':
    company = russia()