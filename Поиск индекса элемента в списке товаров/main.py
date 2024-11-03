# TODO Напишите функцию для поиска индекса товара
def finding_item(shop_list, item):
    for i in shop_list:
        if i == item:
            return shop_list.index(i)

# витрина магазина
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# товары, которые чел хочет купить
items_to_find = ['банан', 'груша', 'персик']

for find_item in items_to_find:
    index_item = finding_item(shop_list=items_list,item=find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
