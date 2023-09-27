# p6.py
# Michael, Martinez
# 9/5/2023
# Python 3.11.5
# Description:This code snippet prompts the user to enter their height in feet and inches, converts the height to inches, rounds the total inches, and then prints the original height in feet and inches along with the rounded total inches.

#for imports>>> pip install measurment

# Prompt the user to enter their height in feet and inches.
print ("Please enter your height")
feet = float(input ("Feet:"))
inches =  float(input ("Inches:"))

# Calculate the total height in inches by converting feet to inches. 
from measurement.measures import Distance
total_inches = Distance(ft=feet).inch 

# Round the total height to the nearest whole inch and adding the remaining inches.
rounded_inches = (round (total_inches) + inches)

# Display the converted height in a user-friendly format.
print(f"{feet} feet {inches} inch(es) = {rounded_inches} inches")

'''
Results
________________________________________________________________
11.exe "c:/Users/pumas/School/cs/week 2/p6.py"
Please enter your height
Feet:6
Inches:0
6 feet 0 inch(es) = 72 inches
'''