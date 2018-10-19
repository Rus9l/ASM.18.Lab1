from .parentclass import Vehicle
from .childclass import Airlane
import pickle

class Container:
      def __init__(self):
          self.list=[]

      def addVehicle(self):
          self.list.append(Vehicle())

      def addAirlane(self):
          self.list.append(Airlane())

      def printlist(self):
          if not self.list:
              print('No list')
              return

          for elem in self.list:
              elem.get()

      def clearlist(self):
         self.list.clear()

      def remove_elem(self):
          print('Number of element?')
          number=int(input())
          if (number <= len(self.list)):
              del self.list[number-1]
          else:
              print('No element')
               
      def edit_elem(self):
         print('Number of element?')
         number=int(input())
         if (number <= len(self.list)):
             self.list[number-1].set()
         else:
              print('No element')
              
      def recording(self):
         with open('outfile','wb') as fp:
             pickle.dump(self.list,fp)

      def read(self):
          with open ('outfile', 'rb') as fp:
              self.list.extend(pickle.load(fp))
    
          

    
