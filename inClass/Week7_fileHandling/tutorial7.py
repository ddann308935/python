shoppingList = []

shoppingListFile = open("shoppingList.txt", "w") # open txt file with write option

while True:
    newItem = input("What do you need to buy? ")
    if newItem == "":
        break
    shoppingList.append(newItem) # add newItem to the list
    shoppingListFile.write(newItem + '\n') # newItem overwrites the txt file

shoppingListFile.close() # close txt file

print(shoppingList) # prints the list

sl = open("shoppingList.txt", "r") # open txt file with read option

#slist = sl.read() # create a variable that holds the txt file

#print(slist) # prints the txt file

slist = sl.readline() # create a variable that holds a line of string in the txt file (1st line)

while slist != "":
    print(slist.strip()) # prints a line from the txt file # strip() removes whitespace
    slist = sl.readline() # moves to the next line in the txt file