from company import country


def add_food(some_company: object):
	while True:
		print('\nChoice country')
		print('1-Russia')
		print('2-No Russia')
		print('0-Back to menu')
		
		try:
			variable = int(input())
			if variable == 0:
				break
			if variable ==1:
				some_company.add_food_r()
				break
			if variable ==2:
				some_company.add_food()
				break
		except ValueError:
			print('\Choice a number')
def edit_food(some_company: object):
    if len(some_company.storage) == 0:
        print ('\nStorage is empty')
        return
    print('\nChoose ID of food to edit in'.format(1,len(some_company.storage)-1))

    try:
        variable = int(input())
        if variable in range(len(some_company.storage)):
            print(some_company.storage[variable])
            some_company.storage[variable].reading()
        else:
            print('No ID')

    except ValueError:
        print('\nType ID please')

def delete_food(some_company: object):
    if len(some_company.storage) == 0:
        print('\nStorage is empty')
        return

    print('\nChoose food to delete '.format(1, len(some_company.storage)))
    
    try:
        variable = int(input())

        if variable in range(len(some_company.storage)):
            some_company.delete_food_from_menu(variable)
        else:
            print('No ID found')

    except ValueError:
        print('\nType a number, please')


def print_storage(some_company: object):
    if len(some_company.storage) == 0:
        print('\nStorage is empty\n')
        return
    else:
	    some_company.print_storage()


def save_to_file(some_company: object):
    if len(some_company.storage) == 0:
        print('\nStorage is empty\n')
        return

    some_company.write_to_file()


def load_from_file(some_company: object):
    some_company.load_from_file()


def erase_storage(some_company: object):
    some_company.clean_storage()





def menu():
	some_company=country()
	
	choice = {
		1:add_food,
        2:edit_food,
        3: delete_food,
        4: print_storage, 
        5: load_from_file,
        6: save_to_file,
        7: erase_storage
	}
	
	
	
	while True :
		print('-----MENU-----')
		print("1- Add food")
		print("2- Edit Food")
		print("3- Delete Food")
		print("4- Print price")
		print("5- Load price")
		print("6- Save price")
		print("7- Erase list")
		print("0- Exit")
		
		
		try:
			variable = int(input())
			if variable == 0:
				break
			if variable in range(len(choice)+1):
				choice[variable](some_company)
		except ValueError:
	   		print('\nType a number, please')
	   	

        


def main():
    menu()
    group().f()


if __name__ == '__main__':
	menu()