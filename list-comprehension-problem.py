# Take the list below and
# 1º make a hard copy
# 2º multiply the prices by 10%
# 3º sort the list inversely from the product name
# 4º sort products by their price
# copy, sorted, produtos.sort

products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

import copy
import operator

""" Part 1 - Increasing Prices by 10% """
new_list = [
    {**x, "price": ("{:.2f}".format(x["price"] * 1.1))} for x in copy.deepcopy(products)
    ]
print("The list with the new prices is:", *new_list, sep="\n")
print()

""" Part 2 - Sorting inversely from the name of products """
products_decreasing_order = sorted(
        copy.deepcopy(new_list),
        key=operator.itemgetter("name"), reverse=True
        )
print("The list with the inversed order is:", *products_decreasing_order, sep="\n")
print()

""" Part 3 - Sorting products by their price """
products_by_price = copy.deepcopy(new_list)
products_by_price = sorted(
    copy.deepcopy(new_list),
    key=operator.itemgetter("price"),
)
print("The list with the order sorted by price is:", *products_by_price, sep="\n")