# coding: utf-8
def open_cookbook():
    arr_of_lines = []
    with open('cookbook.txt', encoding='utf8') as f:
        for line in f:
            arr_of_lines += [line]
    return arr_of_lines


def del_first(arr_of_lines):
    return arr_of_lines.remove(arr_of_lines[0])


def read_dish(arr_of_lines, cook_book):
    if arr_of_lines[0] == '\n':
        del_first(arr_of_lines)
    name_dish = arr_of_lines[0][:len(arr_of_lines[0])-1].lower()
    del_first(arr_of_lines)
    cook_book[name_dish] = []
    count_ing = int(arr_of_lines[0])
    del_first(arr_of_lines)
    for i in range(count_ing):
        cook_book[name_dish] += [{'ingridient_name': '', 'quantity': '', 'measure': ''}]
        ing = arr_of_lines[0]
        del_first(arr_of_lines)
        b = ing.split(' | ')
        cook_book[name_dish][i]['ingridient_name'] = b[0]
        cook_book[name_dish][i]['quantity'] = int(b[1])
        cook_book[name_dish][i]['measure'] = b[2][:len(b[2])-1]
    return arr_of_lines, cook_book


def collect_dishes():
    arr_of_lines = open_cookbook()
    cook_book = dict()
    n = arr_of_lines.count('\n')
    for _ in range(n+1):
        arr_of_lines, cook_book = read_dish(arr_of_lines, cook_book)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = collect_dishes()
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
