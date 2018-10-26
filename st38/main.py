from .conteiner import Container

con=Container()

def add():
    while 1:
        print('1-Vehicle')
        print('2-Airlane')

        try:
            i=int(input())
            if i==1:
                 con.addVehicle()
                 break
            if i==2:
                 con.addAirlane()
                 break
        except ValueError:
            print('Choose number')
            

multiple={
    1:add,
    2:con.edit_elem,
    3:con.remove_elem,
    4:con.printlist,
    5:con.recording,
    6:con.read,
    7:con.clearlist
}
        


def main():
    while 1:
            print('1-Add')
            print('2-Edit')
            print('3-Remove')
            print('4-Print list')
            print('5-Save to file')
            print('6-Load from file')
            print('7-Clear list')
            try:
                 id=int(input())
                 mult=multiple[id]()
  
            except KeyError:
                 print('Choose number')
       
                                    

if __name__ == "__main__":
    main()
