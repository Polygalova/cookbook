def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_cook_book(dishes)
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


def get_cook_book(dishes_list):
    dishes = set(dishes_list)
    cook_book = {}
    for dish in dishes:
        cook_book[dish] = []
    with open('cookbook.txt', encoding='utf8') as f:
        for line in f:
            if line.lower().strip() in dishes:
                quan_ing = int(f.readline().strip())
                for i in range(quan_ing):
                    ing, quan, meas = f.readline().strip().split(' | ')
                    cook_book[dish].append({'ingridient_name': ing, 'quantity': int(quan), 'measure': meas})
    return cook_book


create_shop_list()
