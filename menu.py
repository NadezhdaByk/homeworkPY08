import print_all as pa
import find_sched as fsch
import find_room as fr
import loggiter as log


def start():
    var = input('Добро пожаловать!\nЕсли Вы хотите ввести новую информацию введите 1\nЕсли Вы хотите найти информацию введите 2\n')
    if var == '2':
        var2= input('Ведите цифру выбора\n1- Распечатать расписание учителя\n2- Распечатать общее расписание\n3- Вывести какой урок в это время в кабинете\n')
        if var2=='1':
            name=input('Введите имя преподавателя: ')
            id_name=fsch.find_id(name)
            print(id_name)
            if id_name=='':
                print("Такого преподавателя нет в нашей школе")
            else:
                fsch.find_data(id_name,name)
        if var2=='2':
            pa.find_all()
        if var2=='3':
            less=input("Введите номер урока:\n1: 9-00 - 9-45\n2: 10-00 - 10-45\n3: 11-00 - 11-45\n4: 12-00 - 12-45\n")
            room=input('Введите номер кабинета\n')
            fr.find_room(less,room)

    if var == '1':
        var2= input('Что Вы хотите сделать?\n1- Ввести информацию про нового учителя\n2- Ввести информацию в расписание\n')
        if var2=='1':
            log.log_teach()
        if var == '2':
            log.log_sched()
       
