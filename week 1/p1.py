# p1.py
# Michael Martinez
# 8/29/23
# Python 3.11.5
# Description: program to show output in Python

print ('hello world') # single quote
print ("Hello, world") # doube quote
print ("he\nlo") # \n insert a new line (same as pressing Enter)
# VARIABLES are named storage locations for numbers, strings, lists
# STRING is anything enclosed in quotes "Hello World", that's a string
# NUMBER can be either a FLOAT (Ex: 9.3) or an INTEGER (Ex: 9.0)
# LISTS are things like [1,2,3] or ["Alex", "Stoykov"]
myName = "Alex" # declare/initialize string variable myName
Weight = 183.5483 # declare/initialize float variable Weight
Age = 33 # declare/initialize int variable Age
Grades = [90,77,88]
nameZ = ["Alex", "Stoykov"]

print ("Hello ", myName)
print ("Your weight is ", Weight, "and your age is ", Age)
print ("Your weight is %.2f and your age is %i" %(Weight, Age))
print ("Lists: grades =",Grades,"nameZ=",nameZ)
print ("This is how you print", end=' ')
print ("on the same line")

'''
PS C:\Users\pumas> & C:/Users/pumas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/pumas/School/cs/# p1.py"
hello world
Hello, world
he
lo
Hello  Alex
Your weight is  183.5483 and your age is  33
Your weight is 183.55 and your age is 33
Lists: grades = [90, 77, 88] nameZ= ['Alex', 'Stoykov']
This is how you print on the same line
'''