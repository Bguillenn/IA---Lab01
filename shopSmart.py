"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""

import shop

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"

    option = None
    price = 999999999.0


    for shop in fruitShops:
        currentShopPrice = shop.getPriceOfOrder(orderList)
        if  currentShopPrice < price:
            price = currentShopPrice
            option = shop


    return option

if __name__ == '__main__':
    """
    orders = [('apples',1.0), ('oranges',3.0)]
    dir1 = {'apples': 2.0, 'oranges':1.0}
    shop1 =  shop.FruitShop('shop1',dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2',dir2)
    shops = [shop1, shop2]
    print ("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples',3.0)]
    print ("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    """

    #CUESTIONARIO
    print("\n CUESTIONARIO")
    orders1 = [('apples' , 1.0), ('oranges', 3.0)]
    orders2 = [('apples', 3.0)]
    dir1 = {'apples':2.0, 'oranges':1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples':1.0, 'oranges':5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]


    print("A) ", shopSmart(orders1, shops) == shop1)
    print("B) ", shopSmart(orders2, shops) == shop2)