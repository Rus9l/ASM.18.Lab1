from .container import Group

newGroup = Group()

menuList = [newGroup.addStudent, 
newGroup.addCaptain, 
newGroup.editStudent, 
newGroup.showStudent, 
newGroup.showAllStudents, 
newGroup.deleteStudent, 
newGroup.deleteAllStudents, 
newGroup.saveToFile, 
newGroup.addFromFile]

  
def main():  
    while 1:
        print('\n\n============LEVOCHKO============\n\n' + 
        '1. Добавить студента в группу\n' + 
        '2. Добавить старосту в группу\n' + 
        '3. Редактировать информацию о студенте \n' + 
        '4. Показать информацию о студенте\n'
        '5. Показать информацию о всех студентах\n' + 
        '6. Удалить студента из группы\n' +
        '7. Удалить всех стдентов\n' +
        '8. Сохранить в файл\n' +
        '9. Считать из файла\n' +
        '0. Выйти\n\n===============================\n')

        a = int(input())

        if a != 0:
            try:
                menuList[a - 1]()
            except IndexError:
                print('Введите число от 0 до 9')
        else:
            break
        
if __name__ == '__main__':
    menu()        