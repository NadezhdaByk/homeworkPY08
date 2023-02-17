def find_all():
    f=open('Recipes.csv', 'r', encoding='UTF-8')
    all_data=f.read().split('\n')
    # print(all_data)
    for i in range(len(all_data)-1):
        print_all=all_data[i].split(';')
        print(print_all)
       
    f.close()