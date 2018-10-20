class booking:
	def  __init__(self):
		print('Enter details:')
		self.read()

	def read(self):
		self.name = input('Name: ')
		self.time = input('Time: ')

	def print(self):
		print('Name:', self.name)
		print('Time:', self.time)
		
