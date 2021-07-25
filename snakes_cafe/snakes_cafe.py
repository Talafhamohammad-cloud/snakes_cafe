print("""
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
menu = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado",
        "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]
your_order=[]        
i = 1
order = input(">")
print(f"{i} order of {order} have been added to your meal ")
your_order.append(order)

while True:
  print("would you like to order any things else")
  order = input(">")
  if order.lower() == "n":
    break
  i += 1
  print(f"{i} order of {order}  have been added to your meal")
  your_order.append(order)
  
print(f'your order is {your_order}')
print("thank you\n your order will be ready soon")  






