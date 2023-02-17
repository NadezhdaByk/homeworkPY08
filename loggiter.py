import input_recipe as inprcp

def log_recipe():
    head=inprcp.input_heading()
    
    text=inprcp.input_recipe()
    date=inprcp.input_date()    
    with open('Recipes.csv', 'r+', encoding='UTF-8') as file:
        all_data=file.read().split('\n')
        id_recipe=len(all_data)-1
        file.write(f'{id_recipe};{head};{text};{date}\n')



