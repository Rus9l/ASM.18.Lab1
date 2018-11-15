class ant:
    def __init__(self):
	
        print("Введите пол:")
        self.ant_gender = input()
	
        print("Введите главную функцию для этого муравья:")
        self.ant_responsibility = input()
		
        print("Введите дополнительные обязанности:")
        self.ant_addition_work = input()
		
      
    def output(self):
        print("Пол:",self.ant_gender)
        print("Обязанности муравья:", self.ant_responsibility)
        print("Дополнительные:", self.ant_addition_work)

	