import datetime

def change_recipe(head,recipe):
    # lines = []
    with open ('Recipes.csv', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        # print(lines)
        for i in range(len(lines)):
            data=lines[i].split(';')
            if head==data[1]:
                numline=i
                newrec=[data[0],data[1],recipe,datetime.date.today().strftime("%d-%m-%Y")]
                # print(newrec)
    with open ('Recipes.csv', 'w', encoding='UTF-8') as f:
        for number, line in enumerate(lines):
            if number not in [numline, len(lines)]:
                # print(line)
                f.write(line)
        f.write(f'{newrec[0]};{newrec[1]};{newrec[2]};{newrec[3]}')
    