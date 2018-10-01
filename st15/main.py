from .bank import bank

b = bank()

MENU = [
   ('Заявка виза', b.add_visa),
   ('Заявка мастер', b.add_master),
   ('Вывести список', b.display_list),
   ('Удалить заявку', b.delete),
   ('Изменить заявку', b.edit),
   ('Сохранить в файл', b.save),
   ('Выгрузить из файла', b.load),
   ('Очистить список заявок', b.delete_all)
]




def print_menu():   
        print('______________________________\n')
        for i, item in enumerate(MENU, start=1):
            print('{0}: {1}'.format(i, item[0]))
        print('0: Выход')
        print('______________________________\n')

def main():
    while True:
        print_menu()
        
        try:
            c=int(input('Выберите действие: '))
            if c==0:
                break
            MENU[c - 1][1]()

            
        
        except Exception as ex:
            print(ex)
            print('Все меню на экране')