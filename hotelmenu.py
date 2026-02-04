# Defind the menu of restaurant
menu = {
    'pizza':80,
    'pasta':60,
    'Burger':50,
    'salad':40,
    'coffee':70
}

print("welcome to python restaurent.")
print("pizza: Rs80\n pasta: Rs60\n Burger: Rs50\n salad: Rs40\n coffee: Rs70")

order_total = 0

item_1=input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item{item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not avaialable yet")

    another_order = input('Do you want to add another item? (yes/no) ')
    if another_order == "yes":
        item_2 = input("Enter the name of second item = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item {item_2} has been added to order")
        else:
            print(f"Ordered item {item_2} is not avaiable!")

print(f"the total amount of item to pay is {order_total}")
