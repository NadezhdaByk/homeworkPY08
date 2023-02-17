import datetime
import find_recipe as frcp

def input_heading():
    head=input('Введите название рецепта ')
    item = frcp.find_name(head)
    if item == '1':
        print("Рецепт с таким названием уже есть")
        exit()
    else:
        return head

def input_recipe():
    text=input('Введите рецепт: ')
    return text

def input_date():
    date=datetime.date.today().strftime("%d-%m-%Y")
    return date

