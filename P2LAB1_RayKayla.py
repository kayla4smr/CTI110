#  Kayla Ray
#  6/15/2025
# P2LAB1
# This program will  perform mathematical calulations and displays information to user

#Imort math to use the constant, math.pi
import math

#Get radius from user
radius = float(input("What is the radius of the circle: "))
print()

#calculate diameter
diameter = 2 * radius
print(f"The diameter of the circle is: {diameter:.1f}")
print()

#calculate circumference
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {circumference:.2f}")
print()

#calculate area
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area:.3f}")


