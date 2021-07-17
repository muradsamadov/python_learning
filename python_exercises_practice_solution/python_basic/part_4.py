#  Write a Python program which accepts the radius of a circle from the user and compute the area. 

import math

r = float(input("Input the radius of the circle: "))

Area = math.pi * r**2

print("The area of the circle with radius: " + str(Area))