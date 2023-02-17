def delete_recipe(head):
    with open ('Recipes.csv', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        # print(lines)
        for i in range(len(lines)):
            data=lines[i].split(';')
            if head==data[1]:
                numline=i
    with open ('Recipes.csv', 'w', encoding='UTF-8') as f:
        for number, line in enumerate(lines):
            if number not in [numline, len(lines)]:
                # print(line)
                f.write(line)
        
