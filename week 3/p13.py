# p13.py
# Michael, Martinez
# 9/14/2023
# Python 3.11.5
#Description: Have the user input a amout of cents under 100 and 


def get_total_cents():
    while True:
        try:
            total_cents = int(input("Enter the total amount in cents: "))
            if total_cents < 0 :
                print("Please enter a positive integer under 100 for the total amount.")
            else:
                return total_cents
        except ValueError:
            print("Invalid input. Please enter a valid integer for the total amount.")

def calculate_change(total_cents):
    quarters = total_cents // 25
    total_cents %= 25
    dimes = total_cents // 10
    total_cents %= 10
    nickels = total_cents // 5
    pennies = total_cents % 5
    return quarters, dimes, nickels, pennies

def main():
    total_cents = get_total_cents()
    quarters, dimes, nickels, pennies = calculate_change(total_cents)

    print("\nYour change:")
    if quarters > 0:
        print(f"Quarters: {quarters}")
    if dimes > 0:
        print(f"Dimes: {dimes}")
    if nickels > 0:
        print(f"Nickels: {nickels}")
    if pennies > 0:
        print(f"Pennies: {pennies}")

main()

'''
Enter the total amount in cents: 66

Your change:
Quarters: 2
Dimes: 1
Nickels: 1
Pennies: 1
PS C:\Users\pumas\School\cs> & C:/Users/pumas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/pumas/School/cs/week 3/p13.py"
Enter the total amount in cents: 16

Your change:
Dimes: 1
Nickels: 1
Pennies: 1
PS C:\Users\pumas\School\cs> & C:/Users/pumas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/pumas/School/cs/week 3/p13.py"
Enter the total amount in cents: 6

Your change:
Nickels: 1
Pennies: 1
PS C:\Users\pumas\School\cs> & C:/Users/pumas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/pumas/School/cs/week 3/p13.py"
Enter the total amount in cents: 4

Your change:
Pennies: 4
PS C:\Users\pumas\School\cs> 
'''