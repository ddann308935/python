logfile = open("inClass/Week8_debugging/logfile.txt", 'a')
print("Hello World")

x = 1
if x == 3:
    print("Not the same")
    print("abcdefgh")

newItem = ""

shoppingList = []

logfile.write("At line 13 in module aaa, new Item is " + newItem + "\n")
while newItem != "":
    newItem = input("What do you need to buy? ")
    shoppingList.append(newItem)
print(shoppingList)

logfile.close()

# Debug Technique 1: Walkthrough/ Desk Check
    # Run the program, Error Message, walk through the code

# Debug Technique 2: 

# Debug Technique 3: Log it in a logfile

# Debug Technique 4: 