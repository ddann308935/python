# program to create shopping list

shoppingList = []

shoppingList = ["Milk", "Eggs"]

# print (shoppingList)
shoppingList.append("Flour")
print(shoppingList)

for item in shoppingList:
    #print(item)
    if item == "Eggs":
        print("Sorry, no eggs available today")
        continue
    print("You need to buy: ", item)

print("Head off to the shops")

