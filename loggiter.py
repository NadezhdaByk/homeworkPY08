import input_teacher as inpt
import input_sched as inpsch

def log_teach():
    name=inpt.input_name()
    less=inpt.input_less()    
    with open('Teachers.csv', 'r+', encoding='UTF-8') as file:
        all_data=file.read().split('\n')
        id_teach=len(all_data)-1
        file.write(f'{id_teach};{name};{less}\n')

def log_sched():
    num=inpsch.input_numless()
    num_room=inpsch.input_room()
    less=inpsch.input_less()
    num_class=inpsch.input_class()
    num_less={'1':['9-00','9-45'], '2':['10-00','10-45'], '3':['11-00','11-45'], '4':['12-00','12-45']}    
    with open('Teachers.csv', 'r', encoding='UTF-8') as file:
        all_data=file.read().split('\n')
        for i in range(len(all_data)-1):
            need_less=all_data[i].split(';')        
            if need_less[2]==less:
                id_name=need_less[0]
    if num=='1': 
        time1=num_less['1']       
    if num=='2': 
        time1=num_less['2']       
    if num=='3': 
        time1=num_less['3']
    if num=='4': 
        time1=num_less['4']
    with open('schedule.csv', 'r+', encoding='UTF-8') as file:
        file.write(f'{num};{time1[0]};{time1[1]};{num_room};{less};{num_class};{id_name}\n')

