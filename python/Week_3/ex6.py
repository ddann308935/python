# Fortune Telling

num = int(input("Enter your favourite number from 1 to 50: "))
color = input("Enter your favourite colour out of Red, Grey or Black: ")
dec = float(input("Enter a floating point number from 1 to 10: "))

color = color.lower()
dec = round(dec, 2)

if (num < 9 or color < "grey") and dec == 8.43:
    print("You will win the lottery soon")
elif num != 10 and (color == "red" or dec <= 1.79):
    print("You will live to 110!")
elif num >= 26 and (color == "black" or dec == 8.2):
    print("You will become the next Prime Minister")
else:
    print("I cannot read your fortune")