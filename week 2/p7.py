# p7.py
# Michael, Martinez
# 9/5/2023
# Python 3.11.5
# Description:Calcualte the area and circumference of a circle using the radius
import math #import the math module for more precise pi values

Pi = math.pi #set Pi as new shorter var 

#Ask the user for the radius of the circle
try:
    radius = float(input("What is the radius(in inches) of the circle youd like to draw?: "))

#Validate the input
    if radius <= 0:
        raise ValueError("Number of radius must be a positive integer")
#Set equations
    Circumference = round(2*math.pi*radius, 1) 
    Area = round(math.pi*radius**2, 1)

#print Circumference and Area
    print (f"The Circumference is {Circumference} \nThe Area is {Area}")
except ValueError as e:
    print(f"Error: {e}")

'''
11.exe "c:/Users/pumas/School/cs/week 2/p7.py"
What is the radius(in inches) of the circle youd like to draw?: 632
The Circumference is 3971.0
The Area is 1254827.5
'''