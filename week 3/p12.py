# p12.py
# Michael, Martinez
# 9/13/2023
# Python 3.11.5
# Description: Ask user questions to determin if they can legaly vote

# ask user for input
age = int(input("Please enter your age:"))
citizen = input("Are you a citizen Y/N:")
registered = input("Are you restired to vote Y/N:")


# check if they can vote
if age >=18 and citizen.lower() == 'y' and registered.lower() == 'y':
    print ("You are able to vote, Your vote counts!")
else:
    if age <18:
        print ("\033[91mYou are not old to vote\033[0m")
    if citizen.lower() != "y": 
        print ("\033[91mYou are not a citizen\033[0m")
    if registered.lower() != "y":
        print("\033[91mYou are not registered to vote, once you register you will be able to vote\033[0m")


'''
Please enter your age:20
Are you a citizen Y/N:y
Are you restired to vote Y/N:n
You are not registered to vote, once you register you will be able to vote

PS C:\Users\pumas\School\cs> & C:/Users/pumas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/pumas/School/cs/week 3/p12.py"
Please enter your age:20
Are you a citizen Y/N:n
Are you restired to vote Y/N:n
You are not a citizen
You are not registered to vote, once you register you will be able to vote

PS C:\Users\pumas\School\cs> & C:/Users/pumas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/pumas/School/cs/week 3/p12.py"
Please enter your age:17
Are you a citizen Y/N:n
Are you restired to vote Y/N:n
You are not old to vote
You are not a citizen
You are not registered to vote, once you register you will be able to vote

PS C:\Users\pumas\School\cs> & C:/Users/pumas/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/pumas/School/cs/week 3/p12.py"
Please enter your age:20
Are you a citizen Y/N:y
Are you restired to vote Y/N:y
You are able to vote, Your vote counts!
'''