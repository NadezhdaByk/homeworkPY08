import print_all as pa
import find_recipe as frcp
import loggiter as log
import input_recipe as inprcp
import change_recipe as chrcp
import delete_recipe as dlrcp


def start():
    var = input('Добро пожаловать!\nЕсли Вы хотите ввести новый рецепт введите 1\nЕсли Вы хотите найти рецепт введите 2\nЕсли вы хотите удалить рецепт введите 3\n')
    if var == '2':
        var2= input('Ведите цифру выбора\n1- Изменить рецепт\n2- Показать рецепт\n3- Показать все рецепты\n')
        if var2=='1':
            word=input('Введите название рецепта: ')
            head=frcp.find_word(word)
            # print(head)
            if head=='':
                print("Такого рецепта нет")
            else:
                recipe=input('Введите новый рецепт: ')
                chrcp.change_recipe(head, recipe)
                print('Рецепт изменен')
        if var2=='3':
            pa.find_all()
        if var2=='2':
            var3=input('Поиск по дате - введите 1\nПоиск по названию - нажмите 2\n')
            if var3=='1':
                date=input('Введите дату ')
                # output=frcp.find_date(date)
                # print(output)
                frcp.find_date(date)
            if var3=='2':
                word=input('Введите название ')
                frcp.find_head(word)
                # print(output) 
    if var == '1':
        log.log_recipe()
        print('Новый рецепт добавлен')
    if var == '3':
        word=input('Введите название рецепта: ')
        head=frcp.find_word(word)
            # print(head)
        if head=='':
            print("Такого рецепта нет")
        else:
            dlrcp.delete_recipe(head)
            print('Рецепт удален')
        
       
