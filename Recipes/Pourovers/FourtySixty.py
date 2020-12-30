# Tetsu Kasuya's Award Winning 40/60 Recipe 
# Script by u/ToCans

# Imports
import time

# Initializing
user_check = False
ratio_check = False

# Definitions
def enter_to_cont():
    input("Press Enter to Continue...")

def next_step():
    print("\n****************************************************** \n")

def profile(fourty_pour) :
    question = "Please enter 1, 2, or 3 to determine your coffee's profile:\n\n 1. Bitter\n 2. Sweet\n 3. Balanced\n\nEnter here: "
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
                    bloom1 = fourty_pour * 0.4
                    bloom2 = fourty_pour * 0.6
                    break
            elif prof_num == 3 :
                    bloom1 = bloom2 = fourty_pour * 0.5
                    break
            else :
                print("\nError.")
        except :
            print("\nError.")
    return bloom1,bloom2
   

#def strength(str_num):

print("The 40/60 Pourover Recipe")

# Main Body
# Checks for # of Consumers
while user_check == False:
    users = input("Please input the number of coffee consumers: ")
    try:
        users = int(users)
        user_check = True
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

fourty_pour_init = float(users * ratio * 0.4)
sixty_pour_init = float(users * ratio * 0.6)

# Asks the user for their Coffee Profile Preference
next_step()
print("Would you prefer the profile of your coffee to be bitter, sweet, or balanced?\n")
pour1, pour2 = profile(fourty_pour_init)
