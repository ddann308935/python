# Calculate the volume of a cylinder

import math

R = 5.5
L = 12

area = R * R * math.pi
volume = area * L
area = round(area, 2)
volume = round(volume, 2)

print(f"The area is: {area}")
print(f"The volume is {volume}")