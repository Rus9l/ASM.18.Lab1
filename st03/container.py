from .booking import booking
from .discount import discountbooking
import pickle

class bookings:

	FILE_NAME = "st03/saved"

	def __init__(self):
		self.bookings = []

	def add(self):
		self.bookings.append(booking())

	def adddiscount(self):
		self.bookings.append(discountbooking())

	def print(self):
		if not self.bookings:
			print('List is clear!')
			return False
		i = 1
		for item in self.bookings:
			print('---' + str(i) + '---')
			item.print()
			i+=1
		print('---end---')
		return True

	
	def edit(self):
		if self.print():
			try:
				sw = input("Which one? ")
				self.bookings[int(sw) - 1].read()
			except:
				print('Incorrect input!')

	def delete(self):
		if self.print():
			try:
				sw = input("Which one? ")
				self.bookings.pop(int(sw) - 1)
			except:
				print('Incorrect input!')

	def savetofile(self):
		with open(self.FILE_NAME, "wb") as f:
			pickle.dump(self.bookings, f)

	def loadfromfile(self):
		try:
			with open(self.FILE_NAME, 'rb') as f:
				self.bookings = pickle.load(f)
		except FileNotFoundError:
			print("No saved data found")

	def clear(self):
		self.bookings.clear()