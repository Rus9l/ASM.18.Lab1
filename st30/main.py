from cityResidents import CityResidents

myCity = CityResidents()

      
functions = [myCity.add_human,
           myCity.add_worker, 
           myCity.edit, 
           myCity.delete, 
           myCity.print, 
           myCity.clear,
           myCity.save, 
           myCity.load]

def printMenu():
    print("0 - Exit")
    print("1 - Add human")
    print("2 - Add worker")
    print("3 - Edit residentr")
    print("4 - Remove resident")
    print("5 - Print city residents")
    print("6 - Clear")
    print("7 - Save to base")
    print("8 - Load from base")
    

def main():  
    while True:
        printMenu()
        try:
            i = int(input("№: "))
            if i == 0:
                break
            functions[i - 1]()
        except ValueError:
            print("Error")
        except IndexError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    
if __name__ == '__main__':
	main()