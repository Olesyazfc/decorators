import csv
from datetime import datetime

def logger_path(path):
    def logger(old_funktion):
        def new_funktion(*args, **kwargs):
            name = f'name - {old_funktion.__name__}'
            date = f'date - {str(datetime.now())}'
            result = f'output data - {old_funktion(*args, **kwargs)}'
            arguments = f'arguments - {args}, {kwargs}'
            full_list = [name, date, arguments, result]
            with open (path, 'a') as f: 
                log = csv.writer(f, delimiter=',')
                log.writerow(full_list)
            return full_list
        return new_funktion
    return logger


def my_cook_book():
    cook_book = {}
    with open('C:\Projects\decorators\Recipes.txt', encoding='utf-8') as f:
        for lines in f.read().split('\n\n'):
            line_list = lines.split('\n')
            name = line_list[0]
            qt = int(line_list[1])
            ingredients = line_list[2:qt+2]
            ingredients_list = []
            for ingredient in ingredients:
                ingredient_name, quantity, measure = ingredient.split('|')
                a = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                ingredients_list.append(a)
            cook_book[name] = ingredients_list   
    return cook_book

@logger_path('C:\Projects\decorators\decorat.csv')
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = my_cook_book()
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients_list = cook_book.get(dish)
            for ingredient in ingredients_list:
                ingredient_name = ingredient.get('ingredient_name')
                measure = ingredient.get('measure')
                quantity = ingredient.get('quantity')
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': int(quantity) * person_count}
                else:
                    dict_ing = shop_list.get(ingredient_name)
                    safe_quantity = int(dict_ing.get('quantity'))
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': int(quantity) * person_count + safe_quantity}                                 
    return shop_list             

                
            




# print(my_cook_book())     
print()
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))  