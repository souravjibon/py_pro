#define the menu of restaurant
menu={'Pizza': 100,
      'Pasta': 120,
      'Burger':80,
      'Salad':150,
      'Coffee':60,
      'Chicken Fry':150
}
#Greet
print("Welcome to our restaurant SILICON")
print("Pizza: Tk 100 \nPasta: Tk 120 \nBurger: Tk 80 \nSalad: Tk 150 \nCoffee: Tk 60 \nChicken Fry: Tk 150")
order_total=0
item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")
another_order=input("Do you want to add another item?(Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the second item=")
    if item_2 in menu:
       order_total+=menu[item_2]
       print(f"Item {item_2} has been added to order")
    else:
       print(f"Ordered item {item_2} is not available")
print(f"The total amount of items to pay is {order_total}")