# Import stadndard libraries
import time, random, sys, os
# Import third-party libraries
from pyfiglet import Figlet
from password_generator import PasswordGenerator

# Copywrite information
copyrigth = "© michi 2021-2021"

f = Figlet(font='slant')
print(f.renderText('PUB'))

if sys.platform == 'win32':
    clear_command = 'cls'
else:
    clear_command = 'clear'

print("Loading...")
time.sleep(2)

    
def countdown():
    os.system(clear_command)
    print(f.renderText('COUNTDOWN'))
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins,secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print('Timer completed!')
    #We ask the lengh
    t = input('Enter the time in seconds: ')
    #We print the timer
    countdown(int(t)) 

def passwordGenerator():
    os.system(clear_command)
    print(f.renderText('PASSWORD GENERATOR'))
    pwo = PasswordGenerator()
    password = pwo.generate_password()
    print("Your password is: ", password)
    

def checkLeapYear():
    os.system(clear_command)
    print(f.renderText('CHECK LEAP YEAR'))
    year = int(input("Enter a year:- "))   # Here, you take the input from the user
    if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):   # Here, you check if the year is a leap year
        print("{0} is a leap year!!".format(year))  # Here, you print the year
    else:
        print("{0} is not a leap year!!".format(year))

def help():
    os.system(clear_command)
    print(f.renderText('HELP'))
    available = {
        "Countdown",
        "Check leap year",
        "Password generator"
    }
    info = """
PUB Copyright (c) 2021-present micziz
PUB is free software: \nyou can redistribute it and/or modify under the terms of the BSD 2-Clause "SIMPLEFIED" License.
PUB is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; \nwithout even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
More iformation about the license can be found in the COPYING file.
Contribute to the project by visiting:\nhttps://github.com/micziz/PUB
If you have any questions/issues, please contact me at: \nmiczicontent@gmail.com\nor by opening an issue on GitHub.
Thank you for using PUB!
    """
    selectHelp = input("Enter available to learn about available commands, or info for some general info: ")
    if selectHelp == "available":
        for i in available: print(i)
        input("Press enter to continue...")
    elif selectHelp == "info":
        print(info)
        input("Press enter to continue...")
    else:
        print("Invalid input")
        time.sleep(1)

while True:
    os.system(clear_command)
    print(f.renderText('MAIN MENU'))
    pubChoose = input("Hello and welcome to PUB or Python Utility Bot\nSelect an option: ")
    if pubChoose == "countdown":
        countdown()
    elif pubChoose == "check leap year":
        checkLeapYear()
    elif pubChoose == "password generator":
        passwordGenerator()
    elif pubChoose == "help":
        help()
    elif pubChoose == "exit":
        print("Exiting...")
        time.sleep(1)
        break
    else:
        print("Invalid input")
        time.sleep(1)