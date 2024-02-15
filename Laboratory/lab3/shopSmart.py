# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop


def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"
    
    min_cost = 1000
    min_shop = None
    for shop in fruitShops:
        cost = 0
        for fruit,quantity in orderList:
            if fruit in shop.getAllFruits():
                cost += shop.fruitPrices[fruit]*quantity
            else:
                cost = -1
                break

        print(cost)
        if cost < min_cost and cost != -1: 
            min_cost = cost
            min_shop = shop 


    return min_shop


if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    print(shop1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    
    dir3 = {'mango': 10.0, 'oranges': 8.0}
    shop3 = shop.FruitShop('shop3', dir3)

    dir4 = {'oranges': 10.0}
    shop4 = shop.FruitShop('shop3', dir4)

    shops = [shop1, shop2, shop3, shop4]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())

    print(shop1)

    print("is shop1 = shop2 ? ")
    print(shop1.__eq__(shop2))

    print("is shop1 = shop3 ? ")
    print(shop1.__eq__(shop3))

    print("is shop1 = shop4 ? ")
    print(shop1.__eq__(shop4))

# e2
# 2.a 
# gelAllFruits in shop.py
# 2.b 
# add self.printFruits() in __str__
# 2.c __eq__ & equalCriteria in shop.py
# 2.d in shopSmart
