Greetings = '''Hello <|NAME|>,
Welcome to our stores 
wish you happy shopping
'''
name = input("Your name please\n")
Greetings = Greetings.replace("<|NAME|>", name)
print(Greetings)

items = {
    "Biscuit": {"parle": 20,"britannia":21,"sunfeast":23},
    "Milk": {"amul":25,"mother dairy":26},
    "Chocolate": {'kitkat':50,"cadbury":60,"5 star":15}
}
print("Available items today are ", items.values())

grocery_item = {}
grocery_history = []
stop = False

while not stop:
    name = input("item_name:\n")
    quantity = input("Quantity purchased:\n")
    cost = input("price per item:\n")

    grocery_item = {"item_name": name, "quantity": int(quantity), "cost": float(cost) }
    grocery_history.append(grocery_item)

    response = input("would you like to add some other item as well?\nType 'Y' for continue or 'N' to move to billing:\n")


    if response == 'N' :
        stop = True

grand_total = 0

for item in grocery_history:
    item_total = item['quantity'] * item['cost']
    grand_total += item_total #if we want to keep coding lesser or simple you can add values directly without assigning the variable by giving += operator together
    print("%d %s @ $%.2f $%.2f" %(item['quantity'], item['item_name'], item['cost'], item_total)) #to match the output information like 1 oil @ $1.42 we use this signs in the code

    item_total = 0

print("Grand Total: $%.2f" % grand_total)