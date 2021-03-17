from pprint import pprint

# TODO: Должен получится следующий словарь
'''
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
'''


def cook_book_from_file(path, seek):
    splited = '|'
    lst = list()
    cook_book = {}
    # Прочитал чтобы посмотреть сколько в файле строк.
    with open(path) as f:
        total_lines = sum(1 for _ in f)
    # Открываю и считываю данные в словарь.
    with open(path, 'r', encoding="utf-8") as f:
        dish_name = []
        if total_lines >= seek:
            for line in f.readlines()[seek:]:

                if len(line.strip()) != 1 and '|' not in line:
                    # print(i, line.strip())
                    dish_name.append(line.strip())
                    # cook_book[dish_name] = []

                if len(line.strip()) == 1:
                    count = int(line.strip())
                    # print(i, line.strip())

                if splited in line:
                    # print(i, line.strip())
                    lst.append(line.strip())

                if len(line.strip()) == 0:
                    break

                seek += 1
            ing_list = list()
            for j in range(count):
                ingr_dict = {}
                ingr = lst[j]
                spl = ingr.split(' | ')
                ingr_dict["ingredient_name"] = spl[0]
                ingr_dict["quantity"] = int(spl[1])
                ingr_dict["measure"] = spl[2]
                ing_list.append(ingr_dict)
            cook_book[dish_name[0]] = ing_list
            # pprint(cook_book)
            # cook_book_from_file(path, seek + 1)
    return cook_book, seek


# TODO: Нужно написать функцию, которая на вход принимает список блюд из
#  cook_book и количество персон для кого мы будем готовить

def get_shop_list_by_dishes(dishes, person_count):
    pass


# TODO: На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова

# def get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2):
#     pass


if __name__ == '__main__':
    filename = "recipes.txt"
    a , jj = cook_book_from_file(path=filename, seek=13)
    pprint(a)
    pprint(jj)
