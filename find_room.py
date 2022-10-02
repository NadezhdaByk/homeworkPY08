def find_room(less,room):
    f=open('schedule.csv', 'r', encoding='UTF-8')
    all_data=f.read().split('\n')
    # print(all_data)
    count=0
    for i in range(len(all_data)-1):
        need_less=all_data[i].split(';')
        # print(need_id)
        if need_less[0]==less and need_less[3]==room:
            count = 1
            print(f'в кабинете {need_less[3]} c {need_less[1]} до {need_less[2]} будет {need_less[4]} у {need_less[5]} класса')
    if count == 0:
        print("в этом кабинете в это время нет уроков")

    f.close()
