from pprint import pprint
import os

# Задача №1 - Собираем словарь из файла recipes.txt

with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        recipes = []
        dish_name = f.readline().strip()
        num = int(f.readline().strip())
        for _ in range(num):
            ingrid_list = f.readline().split(' | ')
            recipes.append({'ingredient_name': ingrid_list[0],
                           'quantity': int(ingrid_list[1]),
                           'measure': ingrid_list[2].rstrip()})
        cook_book[dish_name] = recipes

# Задача №2 - считаем количество ингридиентов для блюда исходя из количества персон

def get_shop_list_by_dishes(dishes_list, person_count):
    """This function get a list (!) with one or more dish and quantity of guests and return quantity of ingredients"""
    final_dict = {}
    for dish in dishes_list:
        if dish in cook_book:
            for el in cook_book[dish]:
                middle_dict = {'quantity': el['quantity'] * person_count, 'measure': el['measure']}
                final_dict[el['ingredient_name']] = middle_dict
        else:
            print(f'Блюдо {dish} не в списке.')
    return final_dict

# Задача №3 - Объединяем файлы

with open('1.txt', 'r', encoding='utf-8') as file_1:
    file_list_1 = file_1.readlines()
    name_1 = os.path.basename(r'TASK 3. 28.08.22\1.txt')

with open('2.txt', 'r', encoding='utf-8') as file_2:
    file_list_2 = file_2.readlines()
    name_2 = os.path.basename(r'TASK 3. 28.08.22\2.txt')

with open('3.txt', 'r', encoding='utf-8') as file_3:
    file_list_3 = file_3.readlines()
    name_3 = os.path.basename(r'TASK 3. 28.08.22\3.txt')

temp_dict = {name_1: file_list_1, name_2: file_list_2, name_3: file_list_3}
sorted_tuple = sorted(temp_dict.items(), key=lambda x: len(x[1]))
sorted_dict = dict(sorted_tuple)

with open('result_text.txt', 'w', encoding='utf-8') as final_file:
    for key, value in sorted_dict.items():
        print(key)
        for i in range(len(value)):
            print(f'Строка {i + 1} файла {key}')
            final_file.write(f'Строка {i + 1} файла {key} - {value[i]}')


# # Тестируем Задача №1
pprint(cook_book)
#
# # Тестируем Задача №2
res = get_shop_list_by_dishes(['Фахитос'], 4)
pprint(res)

# Тестируем Задача №3
# pprint(final_file)