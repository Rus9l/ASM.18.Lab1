from .booking import booking

class discountbooking(booking):
	def __init__(self):
		self.read()

	def read(self):
		booking.read(self)
		self.discount = input('Discount: ')

	def print(self):
		booking.print(self)
		print('Discount:', self.discount)