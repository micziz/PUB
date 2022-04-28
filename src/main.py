# Import stadndard libraries
import time, math, random, sys, os
# Import third-party libraries
from pyfiglet import Figlet

# Copywrite information
copyrigth = "© michi 2021-2021"

f = Figlet(font='slant')
print(f.renderText('PUB'))

if sys.platform == 'win32':
    clear_command = 'cls'
else:
    clear_command = 'clear'


pubChoose = input("Hello and welcome to PUB or Python Utility Bot\nSelect an option:")

def guessTheNumber():
    os.system(clear_command)
    f.renderText('GUESS THE NUMBER')

if pubChoose == "guess the number":
    print("########################################################################")
    print("                        GUESS THE NUMBER")
    print("########################################################################")
    #We generate the random number
    number = random.randint(1, 9)
    #We set the chances
    chances = 0
    print("Guess a number (between 1 and 9):")

    #Main while loop
    while True:
        # Enter a number between 1 to 9
        guess = int(input())
        #If the number  is equal to the guess
        if guess == number:
            print(f'CONGRATULATIONS! YOU HAVE GUESSED THE NUMBER {number} IN {chances} ATTEMPTS!')
            # Printing final statement using the f-strings method;
            break
        #If the number is smaller
        elif guess < number:
            print("Your guess was too low: Guess a number higher than", guess)
            #We print this
        #Else (So it's grater)
        else:
            print("Your guess was too high: Guess a number lower than", guess)
            #We print this
        # Increase the value of chance by 1
        chances += 1

elif pubChoose == "countdown":
    print("########################################################################")
    print("                        COUNTDOWN")
    print("########################################################################")
    #Main function to calculate the timer
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
elif pubChoose == "Number to word":
    one_digit_words = {
        '0': ["zero"],
        '1': ["one"],
        '2': ["two", "twen"],
        '3': ["three", "thir"],
        '4': ["four", "for"],
        '5': ["five", "fif"],
        '6': ["six"],
        '7': ["seven"],
        '8': ["eight"],
        '9': ["nine"],
    }

    two_digit_words = ["ten", "eleven", "twelve"]
    hundred = "hundred"
    large_sum_words = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion"]

    def converter(n):
        word = []

        if n.startswith('-'):
            word.append("(negative)")
            n = n[1:]
        
        if len(n) % 3 != 0 and len(n) > 3:
            n = n.zfill(3 * (((len(n)-1) // 3) + 1))

        sum_list = [n[i:i + 3] for i in range(0, len(n), 3)]
        skip = False

        for i, num in enumerate(sum_list):
            if num != '000': skip = False
            
            for _ in range(len(num)):
                num = num.lstrip('0')
                if len(num) == 1:
                    if (len(sum_list) > 1 or (len(sum_list) == 1 and len(sum_list[0]) == 3)) and i == len(sum_list) - 1 and (word[-1] in large_sum_words or hundred in word[-1]):
                        word.append("and")
                    word.append(one_digit_words[num][0])
                    num = num[1:]
                    break

                if len(num) == 2:
                    if num[0] != '0':
                        if (len(sum_list) > 1 or (len(sum_list) == 1 and len(sum_list[0]) == 3)) and i == len(sum_list) - 1:
                            word.append("and")
                        if num.startswith('1'):
                            if int(num[1]) in range(3):
                                word.append(two_digit_words[int(num[1])])
                            else:
                                number = one_digit_words[num[1]][1 if int(num[1]) in range(3, 6, 2) else 0] 
                                word.append(number + ("teen" if not number[-1] == 't' else "een"))
                        else:
                            word.append(one_digit_words[num[0]][1 if int(num[0]) in range(2, 6) else 0] + ("ty " if num[0] != '8' else 'y ') + (one_digit_words[num[1]][0] if num[1] != '0' else ""))
                        break
                    else:
                        num = num[1:]
                        continue
                    
                if len(num) == 3:
                    if num[0] != '0':
                        word.append(one_digit_words[num[0]][0] + " " + hundred)
                        if num[1:] == '00': break
                    num = num[1:]
    
            if len(sum_list[i:]) > 1 and not skip:
                word.append(large_sum_words[len(sum_list[i:]) - 2])
                skip = True
        
        word = " ".join(map(str.strip, word))
        return word[0].lstrip().upper() + word[1:].rstrip().lower() if "negative" not in word else word[:11].lstrip() + word[11].upper() + word[12:].rstrip().lower()

    if __name__ == "__main__":
        while True:
            try:
                n = input("Enter any number to convert it into words or 'exit' to stop: ")
                if n == "exit":
                    break
                int(n)
                print(n, "-->", converter(n))
            except ValueError:
                print("Error: Invalid Number!")
elif pubChoose == "Check leap year":
    year = int(input("Enter a year:- "))   # Here, you take the input from the user

    if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):   
        """
        if a year is a multiple of four and a multiple of 100 i.e. if it is a multiple of 400 it is not a leap year
        """
        print("{0} is a leap year!!".format(year))
        """
        printing the output
        """
    else:
        print("{0} is not a leap year!!".format(year))
elif pubChoose == "password generator":
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    special = "@#$%&*"

    # pass_len=random.randint(8,13)  #without User INput
    pass_len = int(input("Enter Password Length"))

    # length of password by 50-30-20 formula
    alpha_len = pass_len//2
    num_len = math.ceil(pass_len*30/100)
    special_len = pass_len-(alpha_len+num_len)


    password = []


    def generate_pass(length, array, is_alpha=False):
        for i in range(length):
            index = random.randint(0, len(array) - 1)
            character = array[index]
            if is_alpha:
                case = random.randint(0, 1)
                if case == 1:
                    character = character.upper()
            password.append(character)


    # alpha password
    generate_pass(alpha_len, alpha, True)
    # numeric password
    generate_pass(num_len, num)
    # special Character password
    generate_pass(special_len, special)
    # suffle the generated password list
    random.shuffle(password)
    # convert List To string
    gen_password = ""
    for i in password:
        gen_password = gen_password + str(i)
    print(gen_password)