# p14.py
# Michael, Martinez
# 9/14/2023
# Python 3.11.5
#Description: When the user enters a date it  will return the zodiac sign for that specific date


import datetime

# Function to validate the date format
def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%m-%d')
        return True
    except ValueError:
        return False

# Get and validate the date input from the user
while True:
    date_input = input("Enter a date (MM-DD): ")
    if is_valid_date(date_input):
        month, day = map(int, date_input.split('-'))
        break
    else:
        print(f"\033[91mInvalid date format. Please use the MM-DD format.\033[0m")

# Store the date as a variable
birthday = date_input

def zodiac(month, day):
    if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 19):
        return "Aries"
    elif (month == 4 and 20 <= day <= 30) or (month == 5 and 1 <= day <= 20):
        return "Taurus"
    elif (month == 5 and 21 <= day <= 31) or (month == 6 and 1 <= day <= 21):
        return "Gemini"
    elif (month == 6 and 22 <= day <= 30) or (month == 7 and 1 <= day <= 22):
        return "Cancer"
    elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 22):
        return "Leo"
    elif (month == 8 and 23 <= day <= 31) or (month == 9 and 1 <= day <= 22):
        return "Virgo"
    elif (month == 9 and 23 <= day <= 30) or (month == 10 and 1 <= day <= 23):
        return "Libra"
    elif (month == 10 and 24 <= day <= 31) or (month == 11 and 1 <= day <= 21):
        return "Scorpio"
    elif (month == 11 and 22 <= day <= 30) or (month == 12 and 1 <= day <= 21):
        return "Sagittarius"
    elif (month == 12 and 22 <= day <= 31) or (month == 1 and 1 <= day <= 19):
        return "Capricorn"
    elif (month == 1 and 20 <= day <= 31) or (month == 2 and 1 <= day <= 18):
        return "Aquarius"
    elif (month == 2 and 19 <= day <= 29) or (month == 3 and 1 <= day <= 20):
        return "Pisces"
    else:
        return "Invalid Date"
        
zodiac_sign = zodiac(month, day)
if zodiac_sign != "Invalid Date":
    print(f"Your zodiac sign is: {zodiac_sign}")
else:
    print("Invalid date.")


'''
Enter a date (MM-DD): 5-18
Your zodiac sign is: Taurus
'''

