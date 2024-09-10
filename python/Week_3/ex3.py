# check number for odd or even

while True:
    num = float(input("Enter a number: "))
    num = round(num, 0)

    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")