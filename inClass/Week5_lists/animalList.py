zoo = ["giraffe", "elephant", "hippo"]
farm = ["cow", "horse", "sheep"]

print(zoo)
zoo.sort()
print(zoo)

zoo.append("panda")
print(zoo)
zoo.append("giraffe")
print(zoo)

print(zoo.index("giraffe"))
print(zoo.index("panda"))

print("Finding all giraffes")
i = 0
for animal in zoo:
    if animal == "giraffe":
        print(i)
    i += 1

print("I have, ", zoo.count("giraffe"), " giraffes in my zoo")

zoo.extend(farm)
print(zoo)

del zoo[2]
print(zoo)

while zoo != []:
    a = zoo.pop() # variable stores popped value
    print (a)
while zoo != []:
    print(zoo[-1])
    del zoo [-1]

print(zoo)
