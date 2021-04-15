
"""
To run this script, type

  python buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """

    totalCost = 0.0
    "*** YOUR CODE HERE ***"

    
    for fruta,cantidad in orderList:
        if fruta not in fruitPrices:
            print("ERROR: La fruta ", fruta, " no esta dentro del catalogo")
            return None
        else:
            totalCost += cantidad * fruitPrices[fruta]


    return totalCost

# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ]
    print ('Cost of', orderList, 'is', buyLotsOfFruit(orderList))


    print("Cuestionario")
    print("A) Price: ", buyLotsOfFruit([('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]))
    print("B) Price: ", buyLotsOfFruit([('apples', 4.0), ('pears', 3.0), ('limes', 2.0)]))
    print("C) Price: ", buyLotsOfFruit([('apples', 1.25), ('pears', 1.50), ('limes', 1.75)]))
