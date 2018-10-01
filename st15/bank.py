import pickle

from .visa import visa
from .master import master

class bank:
    
    
    
    FILENAME = 'st15/list'
    
    
    
    def __init__(self):
        self.list = []
    
    
    
    def add_visa(self):
        v=visa()
        self.list.append(v)
    
    
    
    def add_master(self):
        m=master()
        self.list.append(m)
    
    
    
    def display_list(self):
        if len(self.list)==0:
            print('\nЗаявок нет')
            return
        print('\nСписок заявок:')
        print('------------------------------')
        for p in self.list:
            print('\t', p.__class__.__name__)
            p.display()
            print('------------------------------')
   
    
   
    def delete(self):
        if len(self.list)==0:
            print('\nЗаявок нет')
            return
        
        print('\nСписок заявок:')
        print('------------------------------')
        for p in self.list:
            print('\t', p.__class__.__name__)
            p.display()
            print('------------------------------')
        
        try:
            nomer=int(input('Введите номер заявки или нажмите 0 для возврата: '))
            if nomer==0:
                return
            del self.list[nomer - 1]
            print('\nЗаявка успешно удалена')
        except Exception:
            print('\nНекорректный номер заявки')
    
    
    
    def edit(self):
        if len(self.list)==0:
            print('\nЗаявок нет')
            return
        
        print('\nСписок заявок:')
        print('------------------------------')
        for p in self.list:
            print('\t', p.__class__.__name__)
            p.display()
            print('------------------------------')
        
        try:
            nomer=int(input('Введите номер заявки или нажмите 0 для возврата: '))
            if nomer==0:
                return
            self.list[nomer - 1].read_input()
        
        except Exception:
            print('\nНекорректный номер заявки')
    
    
    
    def save(self):
        with open(self.FILENAME, 'wb') as f:
            pickle.dump(self.list, f, -1)
            print('\nДанные успешно сохранены')
    
    
    
    def load(self):
        try:
            with open(self.FILENAME, 'rb') as f:
                self.list = pickle.load(f)

            print('\nЗагрузка успешно выполнена')
        
        except FileNotFoundError:
            print('\nФайл отсутствует')
    
    
    
    def delete_all(self):
        self.list = []
        print('\nСписок заявок очищен')
            
            
            
            
            