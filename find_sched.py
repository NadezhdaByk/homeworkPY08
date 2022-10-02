
# data='Усманов Е.П.'
def find_id(data):
    count=0
    f=open('Teachers.csv', 'r', encoding='UTF-8')
    all_id=f.read().split('\n')
    for i in range(len(all_id)):
        need_id=all_id[i].split(';')
        if data==need_id[1]:
            return need_id[0]
            count=1
            exit()
    if count == 0:
        return "Такого преподавателя нет в нашей школе"
    f.close()

# print(find_id(data))


def find_data(data_id, data):
    count = 0
    f=open('schedule.csv', 'r', encoding='UTF-8')
    all_data=f.read().split('\n')
    # print(all_data)
    for i in range(len(all_data)-1):
        need_id=all_data[i].split(';')
        # print(need_id)
        if need_id[6]==data_id:
            # print(need_id)
            count = 1
            print(f'Расписание у {data}\n начало урока {need_id[1]}, конец урока {need_id[2]}, кабинет {need_id[3]}, класс {need_id[5]}')
    if count == 0:
        return "У преподавателя нет уроков"

    f.close()
# find_data(find_id(data),data)