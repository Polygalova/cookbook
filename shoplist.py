def get_shop_list():
    n = int(input('Сколько человек?'))
    dishes = set(input('Что будем готовить?').lower().strip().split(', '))
    shop_list = {}
    ing_meas = {}
    with open('cookbook.txt', encoding='utf8') as f:
        for line in f:
            if line.lower().strip() in dishes:
                quan_ing = int(f.readline().strip())
                for i in range(quan_ing):
                    ing, quan, meas = f.readline().strip().split(' | ')
                    if ing not in shop_list.keys():
                        shop_list[ing] = int(quan)
                        ing_meas[ing] = meas
                    else:
                        shop_list[ing] += int(quan)
    for quan in shop_list.values():
        quan *= n
    return shop_list, ing_meas


def print_shop_list():
    shop_list, ing_meas = get_shop_list()
    for ing, quan in shop_list.items():
        print('{} {} {}'.format(ing, quan, ing_meas[ing]))


print_shop_list()
