
#  calculate the area of a rectangle

l = float(input("Please enter the length: "))
w = float(input("Please enter the width: "))

area = round(l * w, 2)

print(f"The area of the rectangle is {area}")



# calculate the area of a circle

import math

r = float(input("Please enter the radius: "))
area = r * r * math.pi
area = round(area, 2)

print(f"The area of the circle is {area}")



# calculate the area and volume of a cylinder

import math

r = float(input("Please enter the radius: "))
l = float(input("Please enter the length: "))

area = r * r * math.pi
area = round(area, 2)

vol = round(area * l, 2)

print(f"The area of the cylinder is {area}")
print(f"The volume of the cylinder is {vol}")




