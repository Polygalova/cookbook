def is_in(shop_list, new_ing):
    for i in range(len(shop_list)):
        if new_ing['ingridient_name'] == shop_list[i]['ingridient_name']:
            return i
    return


def get_shop_list():
    n = int(input('Сколько человек?'))
    dishes = input('Что будем готовить?').lower().strip().split(', ')
    shop_list = []
    with open('cookbook.txt', encoding='utf8') as f:
        for line in f:
            if line.lower().strip() in dishes:
                quan_ing = int(f.readline().strip())
                for i in range(quan_ing):
                    ing, quan, meas = f.readline().strip().split(' | ')
                    new_ing = {'ingridient_name': ing, 'quantity': int(quan), 'measure': meas}
                    result = is_in(shop_list, new_ing)
                    if result is None:
                        shop_list.append(new_ing)
                    else:
                        shop_list[result]['quantity'] += new_ing['quantity']
    for ingredient in shop_list:
        ingredient['quantity'] *= n
    return shop_list


def print_shop_list():
    shop_list = get_shop_list()
    for shop_list_item in shop_list:
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


print_shop_list()
