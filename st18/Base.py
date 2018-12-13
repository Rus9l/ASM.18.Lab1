class russia:
    def reading(self):
	    while True:
	        try:
	        	print("Name food")
	        	self.name = input()
	        	
	        	print("Price food")
	        	self.price = int(input())
	        	break
	        	
	        except ValueError:
	        	print('\nError. Type a number')
    
    
    def printing(self):
        print ('Name: ',self.name)
        print ('Price: ',self.price)

if __name__=='__main__':
    b = russia()
    b.reading()
    b.printing()