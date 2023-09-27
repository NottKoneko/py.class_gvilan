# p15.py
# Michael, Martinez
# 9/14/2023
# Python 3.11.5
#Description: 


def validate_input(input_str):
    try:
        # Split the input string by commas and check if it results in a list of exactly 4 items
        input_values = input_str.split(',')
        if len(input_values) != 4:
            return False
        
        # Attempt to convert each value to a float
        for value in input_values:
            float(value)
        
        return True
    except ValueError:
        return False

while True:
    user_input = input("Enter 4 numbers separated by commas: ")
    if validate_input(user_input):
        a, b, c, d = map(float, user_input.split(','))

        # Define variables
        sum_pos = 0 
        sum_neg = 0

        # Sort and sum the numbers
        for num in [a, b, c, d]:
            if num > 0:
                sum_pos += num
            else:
                sum_neg += num

        break
    else:
        print("\033[91mInvalid input, please try again. Try something like 1,2,3,4\033[0m")

# Print output of each variable
print(f"Sum of positive numbers: {sum_pos}")
print(f"Sum of negative numbers: {sum_neg}")

'''
Enter 4 numbers separated by commas: 1,-1,4,-3
Sum of positive numbers: 5.0
Sum of negative numbers: -4.0
PS C:\Users\pumas\School\cs> 
'''

