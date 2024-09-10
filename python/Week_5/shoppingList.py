shoppingList = []

newItem = "something"

print("After typing your shopping List, press enter only Please")

while True:
    newItem = input("What do you need to buy? ")
    if newItem == "":
        break
    shoppingList.append(newItem)

print(shoppingList)