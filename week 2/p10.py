# p10.py
# Michael, Martinez
# 9/5/2023
# Python 3.11.5
#Description:Make a function to return a letter grade for a given integer

def grade_calculation():
    while True:
        try:
            percent = float(input("Please enter a grade in percent: "))
            if percent < 0 or percent > 100:
                raise ValueError("Percent must be between 0 and 100")
            
            #
            break

        except ValueError as e:
            print(f"Error: {e}")

    #asign the current grade

    if percent >= 90:
        print("Your grade is: A")
    elif percent >= 80:
        print("Your grade is: B")
    elif percent >= 70:
        print("Your grade is: C")
    elif percent >= 60:
        print("Your grade is: D")
    else:
        print("Your grade is: F")

# Call the function to start the input and calculation process
grade_calculation()

'''
sApps/python3.11.exe "c:/Users/pumas/School/cs/week 2/p10.py"'
Please enter a grade in percent: 99
Your grade is: A
'''