

print(
    """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
    """)

menu = ['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat tornado',
            'a literal garden', 'ice Cream', 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']
your_orders = []

ordersNames = []


def ordering():

    order = input('>')
    if order.lower() in menu:
        your_orders.append(order)
        if order not in ordersNames:
            ordersNames.append(order)
        print(
            f'** {your_orders.count(order)} order of {order} have been added to your meal **')
        ordering()
    elif order.lower() == 'quit':
        print('Your order is:')
        for orderList in ordersNames:
            print(f'{your_orders.count(orderList)} order of {orderList} ')
        print('thank you\n your order will be ready soon')
        print('please dont forget to rate us on cafe website')
    elif order.lower() not in menu:
        print(f'sorry {order} is not in our menu')
        ordering()


ordering()
