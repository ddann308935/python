# test for vowel with first character

username = input("Enter a username: ")
vowels = "aeiouAEIOU"

i = 0

while i < len(vowels): 
    if username[0] == vowels[i]:
        print("First letter of ",username, "is a vowel.")
        break
    elif username[0] == vowels[len(vowels) - 1]:
        print("First letter of ",username, "is not vowel.")
        break
    else:
        i += 1
        continue

# if statement for colour

color = input("Enter a color: ")
color = color.lower

if color == "green" or "orange":
    print("You Win!")
else:
    print("Sorry!")


