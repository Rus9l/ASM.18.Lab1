from Base import russia

class norussia(russia):
    def reading(self):
        while True:
            try:
                super().reading()
                print('Region country')
                self.regcountry= int(input())
                break
                
            except ValueError:
                print ('\n Type a number')

    def printing(self):
        super().printing()
        print('Region: ', self.regcountry)


if __name__ == '__main__':
    n = norussia()
    n.reading()
    n.printing()