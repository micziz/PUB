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


def guessTheNumber():
    os.system(clear_command)
    print(f.renderText('GUESS THE NUMBER'))
    def generateNumber(n):
        return random.randint(1, n)
    generatedNumber = generateNumber(10)
    tries = 3
    while tries > 0:
        guess = int(input("Guess the number: "))
        if guess == generatedNumber:
            print(f"You guessed it in {tries} Tries!")
            break
        elif guess > generatedNumber:
            print("Too high!")
            tries -= 1
        elif guess < generatedNumber:
            print("Too low!")
            tries -= 1
    
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

while True:
    os.system(clear_command)
    print(f.renderText('MAIN MENU'))
    pubChoose = input("Hello and welcome to PUB or Python Utility Bot\nSelect an option:")
    if pubChoose == "guess the number":
        guessTheNumber()
    elif pubChoose == "countdown":
        countdown()
    elif pubChoose == "check leap year":
        checkLeapYear()
    elif pubChoose == "password generator":
        passwordGenerator()