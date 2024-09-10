# while statement

count = 1   # loop control variable
x = 2

while count < 11:
    print(x)
    x = x * 2
    count += 1

# while statement sample

import random

count = 1 # declare variables
highest = 0

while count < 11:
    num = random.randint(0, 100) # generate random int
    print(num)
    if num > highest:
        highest = num          # determine highest value
    count += 1                 # increment count

print()
print("The highest number is", highest)