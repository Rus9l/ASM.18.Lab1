import pickle
from ant import ant
from soldier import soldier


class ant_colony:
    def __init__(self):
        self.ants = []

    def add_ant(self):
        self.ants.append(ant())
		
    def add_soldier(self):
        self.ants.append(soldier())
		
    def print_colony(self):
        if len(self.ants) == 0:
            print("В колонии пока нет муравьев")
        else:
            i=0
            for ant in self.ants:
                print(i+1, "муравей")
                ant.output()
                i+=1

    def import_to_file(self):
        with open('ants.pickle', 'wb') as f:
            pickle.dump(self.ants, f)

    def export_from_file(self):
        with open('ants.pickle', 'rb') as f:
            self.ants = pickle.load(f)
			
    def delete_colony(self):
        self.ants.clear()
