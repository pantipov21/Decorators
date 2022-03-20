import HW

PATH = 'files/'
#
#  Задача 1 и ниже задача 2
#
cook_book = dict()


@HW.decorator_log(PATH)
def read_cook_book(filename):
    with open(filename, 'r') as f:
        while True:
            content = '\n'
            while content == '\n':
                content = f.readline()
            if content == '':
                break
            name = content.split("\n")[0] # прочитали название блюда
            number = int(f.readline()) # прочитали количество компонентов
            recipe = list()

            for i in range(0,number):
                recipe_dict = dict()
                data = f.readline()
                ingredient = data.split(" | ", 3)
                recipe_dict['ingredient_name'] = ingredient[0]
                recipe_dict['quantity'] = ingredient[1]
                recipe_dict['measure'] = ingredient[2].split("\n")[0]
                recipe.append(recipe_dict)

            cook_book[name] = recipe
    for k,v in cook_book.items():
        print(f'{k}')
        for v2 in v:
            print(v2)
        print('')


#
# Задача 2
#
@HW.decorator_log(PATH)
def get_shop_list_by_dishes(dishes, person_count):
    res = dict()
    for dish in dishes:
        ingredients = cook_book.get(dish)
        for i in ingredients:
            res[i.get('ingredient_name')] = {'measure': i.get('measure'),
                                             'quantity': person_count*int(i.get('quantity'))}
    for k,v in res.items():
        print(f'{k}:{v}')
    return res



read_cook_book(f'{PATH}recipes.txt')
print('-------------------------------------')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2)
