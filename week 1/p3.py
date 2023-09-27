# p3.py
# Michael, Martinez
# 9/5/2023
# Python 3.11.5
# Description: program to take input in Python

name = input ("Please enter your name:") # this iS a string
weightLbs = float(input ("Please enter your weight in lbs")) # a flaot
age = int (input ("Please enter your age (whole number): ")) # an interger
weightKg = weightLbs*0.453592
title = "Human"

print ("Hello", title, name, "your weight is")
print (weightLbs, "lbs")
print ("which equals = %.2f" %weightKg, end= ' ') # end=' ' prevwnts new line
print ("kilograms ") 

'''
11.exe "c:/Users/pumas/School/cs/week 1/p3.py"
Please enter your name:Koneko
Please enter your weight in lbs180
Please enter your age (whole number): 18
Hello Human Koneko your weight is
180.0 lbs
which equals = 81.65 kilograms

'''