goods_list = []
turn = None
stop = 'q'

while turn != stop:
    item_dict = {
        'название': input('Введите название товара'),
        'цена': input('Введите цену единицы товара'),
        'количество': input('Введите количество единиц товара'),
        'ед': input('Введите единицу измерения товара')
    }
    item = (item_dict)
    type(item)
    print('item')
    goods_list.append(item)

    for item in enumerate(goods_list, 1):
        print(item)

    turn = input('Хотите прекратить ввод товаров нажмите q?')


