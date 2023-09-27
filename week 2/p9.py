# p9.py
# Michael, Martinez
# 9/5/2023
# Python 3.11.5
#Description:

try:
    # Prompt the user to enter height in feet and inches
    input_str = input("Enter your height in feet and inches (X,Y): ")
    
    # Split the input string into feet and inches, and convert them to float
    feet, inches = map(float, input_str.split(','))

    # Create a Distance object and calculate total inches
    total_inches = feet * 12 + inches

    # Determine and print the height category
    if total_inches >= 72:
        print(f"Wow {total_inches} inches! You're tall!")
    elif total_inches > 60 and total_inches < 72:
        print(f"Wow {total_inches} inches! You are of average height. Don't be sad; at least you're not short!")
    elif total_inches <= 60:
        print(f"Wow {total_inches} inches! You are short!")

except ValueError:
    # Handle invalid input with a user-friendly error message
    print('\033[91m' + '\033[1m' + "Try again. Use the format X,Y (e.g., 6,0)" + '\033[0m')


'''
Enter your height in feet and inches (X,Y): 6,5
WoW 77.0 Your Tall!
'''
