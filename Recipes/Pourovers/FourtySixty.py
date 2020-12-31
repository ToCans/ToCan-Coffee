# Tetsu Kasuya's Award Winning 40/60 Recipe 
# Script by u/ToCans

# Imports
import time
import os

# Initializing
user_check = False
gram_check = False
ratio_check = False


# Definitions
###############################
def clear_terminal() :
    os.system('cls' if os.name == 'nt' else 'clear')

def enter_to_cont():
    input("Press Enter to Continue...")

def next_step():
    print("\n****************************************************** \n")

def profile(fourty_pour) :
    question = "\nPlease enter 1, 2, or 3 to determine your coffee's profile:\n\n 1. Bitter\n 2. Balanced\n 3. Sweet\n\nEnter here: "
    prof_num = False
    while prof_num not in [1, 2, 3] :
        prof_num = input(question)
        try :
            prof_num = int(prof_num)
            if prof_num == 1 :
                    bloom1 = fourty_pour * 0.6
                    bloom2 = fourty_pour * 0.4
                    break
            elif prof_num == 2 :
                    bloom1 = bloom2 = fourty_pour * 0.5
                    break
            elif prof_num == 3 :
                    bloom1 = fourty_pour * 0.4
                    bloom2 = fourty_pour * 0.6
                    break
            else :
                print("\nError.")
        except :
            print("\nError.")
    return bloom1,bloom2
   
def strength(sixty_pour) :
    question = "\nPlease enter 1, 2, or 3 to determine the strength of your coffee:\n\n 1. Weak\n 2. Balanced\n 3. Strong\n\nEnter here: "
    str_num = False
    while str_num not in [1, 2, 3] :
        str_num = input(question)
        try :
            str_num = int(str_num)
            if str_num == 1 :
                    pour3 = sixty_pour / str_num
                    pour4 = 0
                    pour5 = 0
                    break
            elif str_num == 2 :
                    pour3 = sixty_pour / str_num
                    pour4 = sixty_pour / str_num
                    pour5 = 0
                    break
            elif str_num == 3 :
                    pour3 = sixty_pour / str_num
                    pour4 = sixty_pour / str_num
                    pour5 = sixty_pour / str_num
                    break
            else :
                print("\nError.")
        except :
            print("\nError.")
    return str_num, pour3, pour4, pour5
###############################

# Main Body
clear_terminal()
print("###########################\nThe 40/60 Pourover Recipe\n###########################\n")
# Checks for # of Consumers
while user_check == False:
    users = input("Please input the number of coffee consumers: ")
    try:
        users = int(users)
        user_check = True
    except:
        print("Error. Please enter a numerical value.\n")

# Checks for the grams of coffee
next_step()
while gram_check == False:
    grams = input("Please input the amount of coffee grams you will use per person: ")
    try:
        grams = float(grams)
        gram_check = True
    except:
        print("Error. Please enter a numerical value.\n")

# Checks for numberical value for ratio
next_step()
while ratio_check == False:
    ratio = input("Please input a coffee ratio from 15 to 17: ")
    try:
        ratio = float(ratio)
        if ratio >= 15 <= ratio <= 17:
            ratio_check = True
        else:
            ratio_check = False
            print("Error. Please enter a numberical value from 15 to 17.\n")
    except:
        print("Error. Please enter a numberical value from 15 to 17.\n")


# Calculaltes 40 and 60 percents 

fourty_pour_init = float(users * grams * ratio * 0.4)
sixty_pour_init = float(users * grams * ratio * 0.6)
total_coffee_grams = float(users * grams)

# Asks the user for their Coffee Profile and Strength Preferences
next_step()
print("Would you prefer the profile of your coffee to be bitter, balanced, or sweet?")
pour1, pour2 = profile(fourty_pour_init)
next_step()
print("Would you prefer the strength of your coffee to be weak, balanced, or strong?")
strength_num, third_pour, fourth_pour, fifth_pour = strength(sixty_pour_init)