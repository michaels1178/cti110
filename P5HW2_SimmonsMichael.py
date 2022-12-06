#This program creates a math quiz generating random numbers
#
#November 29, 2022
#CTI-110 P5HW2 - Math Quiz
#Michael Simmons
#
#The program should open with 3 start menu options.
#The Program menu options are:
    ##-1 Adding Random Numbers
    ##-2 Subtracting Random Numbers
    ##-3 Exit
#For both Adding Random Numbers menu option and Subtracting Random Numbers menu option:
    ##-The program generates two random numbers.
    ##-The program prompts a user to add the two numbers by requesting user input for an answer.
    ##-The progran then decides if the user answer is "Too High" or "Too Low".
    ##-If the answer is correct, the program displays a message of congradulations and displays the number of guesses it took to get the correct answer.
    ##-If the answer is incorrect, the program should notify the user if their answer was too low or too high and ask them to guess again.
    ##-The program will loop until the correct answer is given.
#For the Exit menu option:
    ##-The program displays a message thanks and an outgoing salutation to user
    ##-The program should terminate the math quiz.
#

import random

MIN = 1
MAX = 1000


def main():
    print("Welcome to Math Quiz\n")
    print("MAIN MENU")     
    print("--------------------------------------------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    Menu_Option = int(input("Please choose one of the menu options: "))
    if Menu_Option == 1:
        add()
    elif Menu_Option == 2:
        subtract()
    elif Menu_Option == 3:
        print("Thank you for playing...")
        print("Bye!!")    
        exit()
    else:
        print("\nEnter 1, 2, 3\n")
        main()

def add():
    number1 = random.randint(MIN, MAX)
    number2 = random.randint(MIN, MAX)
    num = number1 + number2
    guesses = 0
    print("--------------------------------------------------------------")
    print("Add these two numbers")
    print(number1, "\n+", number2)
    print("The sum is", num)
    guessing = True
    while guessing:
        guess = int(input("Enter answer.\n"))
        if guess > num:
            print("Sorry, guess is too high!")
            guesses=guesses+1
        elif guess < num:
            print("Sorry, guess is too low.")
            guesses=guesses+1
        else:
            print("Congradulations!!!!!", "your answer is correct..")
            guessing = False
            guesses=guesses+1
            print('Number of guesses: %d ' % guesses)
            print()
            main()
        
def subtract():
    number1 = random.randint(MIN, MAX)
    number2 = random.randint(MIN, MAX)
    num = number1 - number2
    guesses = 0
    print("--------------------------------------------------------------")
    print("Subtract these two numbers")
    print(number1, "\n-", number2)
    print("The difference is", num)
    guessing = True
    while guessing:
        guess = int(input("Enter answer.\n"))
        if guess > num:
            print("Sorry, guess is too high!")
            guesses=guesses+1
        elif guess < num:
            print("Sorry, guess is too low.")
            guesses=guesses+1
        else:
            print("Congradulations!!!!!", "your answer is correct..")
            guessing = False
            guesses=guesses+1
            print ("Number of guesses: %d " % guesses)
            print()
            main()
main()
