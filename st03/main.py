from .container import bookings

def main():
	b = bookings()
	menu = {
		'0':('Exit',None),
		'1':('Add',b.add),
		'2':('Add discounted',b.adddiscount),
		'3':('Edit',b.edit),
		'4':('Delete',b.delete),
		'5':('Show',b.print),
		'6':('Save',b.savetofile),
		'7':('Load',b.loadfromfile),
	}
	while True:
		for li in menu:
			print(li + " " + menu[li][0])
		try:
			sw = input()
			if sw == "0":
				break
			else:
				menu[sw][1]()
		except:
			print('Incorrect input!')