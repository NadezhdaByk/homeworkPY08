import datetime

def find_name(need_word):
    f=open('Recipes.csv', 'r', encoding='UTF-8')
    all_data=f.read().split('\n')
    for i in range(len(all_data)-1):
        data=all_data[i].split(';')
        if need_word==data[1]:
            return '1'
        else:
            return '0'
    f.close()

def find_head(need_word):
    count=0
    f=open('Recipes.csv', 'r', encoding='UTF-8')
    all_data=f.read().split('\n')
    for i in range(len(all_data)-1):
        data=all_data[i].split(';')
        if need_word==data[1]:
            print(data)
            count=1
    if count == 0:
        print("Такого рецепта нет в архиве")
    f.close()

def find_word(need_word):
    count=0
    f=open('Recipes.csv', 'r', encoding='UTF-8')
    all_data=f.read().split('\n')
    for i in range(len(all_data)-1):
        data=all_data[i].split(';')
        if need_word==data[1]:
            return data[1]
    if count == 0:
        print("Такого рецепта нет в архиве")
        exit()
    f.close()

def find_date(date):
    count=0
    f=open('Recipes.csv', 'r', encoding='UTF-8')
    all_data=f.read().split('\n')
    for i in range(len(all_data)-1):
        data=all_data[i].split(';')
        if date==data[3]:
            print(data)
    if count == 0:
        return "Такого рецепта нет в архиве"
    f.close()
