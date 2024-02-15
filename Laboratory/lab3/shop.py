# shop.py
# -------
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


class FruitShop:

    def __init__(self, name, fruitPrices):
        """
            name: Name of the fruit shop

            fruitPrices: Dictionary with keys as fruit
            strings and prices for values e.g.
            {'apples':2.00, 'oranges': 1.50, 'pears': 1.75}
        """
        self.fruitPrices = fruitPrices
        self.name = name
        print('Welcome to %s fruit shop' % (name))

    def getCostPerPound(self, fruit):
        """
            fruit: Fruit string
        Returns cost of 'fruit', assuming 'fruit'
        is in our inventory or None otherwise
        """
        if fruit not in self.fruitPrices:
            return None
        return self.fruitPrices[fruit]

    def getPriceOfOrder(self, orderList):
        """
            orderList: List of (fruit, numPounds) tuples

        Returns cost of orderList, only including the values of
        fruits that this fruit shop has.
        """
        totalCost = 0.0
        for fruit, numPounds in orderList:
            costPerPound = self.getCostPerPound(fruit)
            if costPerPound != None:
                totalCost += numPounds * costPerPound
        return totalCost

    def getName(self):
        return self.name
    
    def printFruits(self):
        for fruit, price in self.fruitPrices.items() : 
            print(fruit, "with price: ", price)

    def getAllFruits(self):
        return self.fruitPrices.keys()


    def equalCriteria(shop1, shop2):

        if not isinstance(shop1 , FruitShop):
            return False
        
        if not isinstance(shop2, FruitShop):
            return False
        
        all_fruits_shop1 = shop1.fruitPrices.keys()

        for fruit in shop2.fruitPrices.keys():
            if not(fruit in all_fruits_shop1):
                return False

        if len(shop1.fruitPrices) != len(shop2.fruitPrices):
            return False
        
        return True


    # returns human readable string representation of an object, called by print(),str(),format()
    def __str__(self):
        self.printFruits()
        return "<FruitShop: %s>" % self.getName()

    # official string representation of an object , called by repr()
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if isinstance(other, FruitShop):
            return self.equalCriteria(other) 
        


f = FruitShop("abc", {"mere":1,"pere":2})
print(f.__dict__)