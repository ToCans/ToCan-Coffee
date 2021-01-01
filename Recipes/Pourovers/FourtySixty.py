# Tetsu Kasuya's Award Winning 40/60 Recipe 
# version 1.0.1
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
    input("When ready, press Enter to continue...")

def next_step():
    print("\n****************************************************** \n")

def profile(fourty_pour) :
    question = "\nPlease enter 1, 2, or 3 to determine your coffee's flavor profile:\n\n 1. Acidic\n 2. Balanced\n 3. Sweet\n\nEnter here: "
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
    next_step()
    return bloom1,bloom2
   
def strength(sixty_pour) :
    question = "\nPlease enter 1, 2, or 3 to determine the strength of your coffee's flavor profile:\n\n 1. Light\n 2. Medium\n 3. Strong\n\nEnter here: "
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
    next_step()
    return str_num, pour3, pour4, pour5  

def countdown(seconds) :
    while seconds > 0 :
        if seconds >= 10 :
            print(str(seconds),end="\r")
            seconds -= 1
            time.sleep(1)
        else :
            print(str(seconds)," ",end="\r")
            seconds -= 1
            time.sleep(1)

def preparations(num_grams,num_water) :
    clear_terminal()
    next_step()
    print("Please prepare", str(round(num_grams,1)),"g of coffee.")
    print("Please prepare", str(round(num_water+100,1)),"ml of water.")
    next_step()
    enter_to_cont()

def rinse(coffee_grams):
    next_step()
    print("PREPARATION:\n\nPlease rinse your filter and pour the", str(round(coffee_grams,1)) + "g"," of coffee grounds into the filter once drained.")
    print("Discard the water from the filter, put your cup and filter on the scale, shake the filter to level off the coffee grounds, and tare the scale.\n")
    enter_to_cont()
    clear_terminal()

def recipe1_summary(pour1,pour2,pour3,tot_coffee_grams) :
    clear_terminal()
    next_step()
    print("SUMMARY:\nThere will be a total of three pours, 45 seconds between the start of each pour.\n")
    print("First pour: " + str(round(pour1,1)) + "g", 
    "\nSecond Pour: " + str(round(pour2,1)) + "g", 
    "\nThird Pour: " + str(round(pour3,1)) + "g\n")
    rinse(tot_coffee_grams)
    return 

def recipe2_summary(pour1,pour2,pour3,pour4,tot_coffee_grams) :
    clear_terminal()
    next_step()
    print("SUMMARY:\nThere will be a total of four pours, 45 seconds between the start of each pour.\n")
    print("First pour: " + str(round(pour1,1)) + "g", 
    "\nSecond Pour: " + str(round(pour2,1)) + "g", 
    "\nThird Pour: " + str(round(pour3,1)) + "g",
    "\nFourth Pour: " + str(round(pour4,1)) + "g\n")
    rinse(tot_coffee_grams)
    return

def recipe3_summary(pour1,pour2,pour3,pour4,pour5,tot_coffee_grams) :
    clear_terminal()
    next_step()
    print("SUMMARY:\nThere will be a total of five pours, 45 seconds between the start of each pour.\n")
    print("First pour: " + str(round(pour1,1)) + "g", 
        "\nSecond Pour: " + str(round(pour2,1)) + "g", 
        "\nThird Pour: " + str(round(pour3,1)) + "g", 
        "\nFourth Pour: " + str(round(pour4,1)) + "g", 
        "\nFifth Pour: " + str(round(pour5,1)) + "g\n")
    rinse(tot_coffee_grams)
    return

def recipe1(pour1,pour2,pour3):
    print("First Pour:", str(round(pour1,1))+"g")
    print("Begin pour in:")
    countdown(10)
    print("Pour to", str(round(pour1,1))+"g")
    countdown(40)
    clear_terminal()
    print("Second Pour:", str(round(pour2,1))+"g")
    print("Begin pour in:")
    countdown(5)
    print("Pour to", str(round(pour1+pour2,1))+"g")
    countdown(40)
    clear_terminal()
    print("Third Pour:", str(round(pour3,1))+"g")
    print("Begin pour in:")
    countdown(5)
    print("Pour to", str(round(pour1+pour2+pour3,1))+"g")
    countdown(45)
    clear_terminal()
    print("Finished!")
    return

def recipe2(pour1,pour2,pour3,pour4):
    print("First Pour:", str(round(pour1,1))+"g")
    print("Begin pour in:")
    countdown(10)
    print("Pour to", str(round(pour1,1))+"g")
    countdown(40)
    clear_terminal()
    print("Second Pour:", str(round(pour2,1))+"g")
    print("Begin pour in:")
    countdown(5)
    print("Pour to", str(round(pour1+pour2,1))+"g")
    countdown(40)
    clear_terminal()
    print("Third Pour:", str(round(pour3,1))+"g")
    print("Begin pour in:")
    countdown(5)
    print("Pour to", str(round(pour1+pour2+pour3,1))+"g")
    countdown(40)
    clear_terminal()
    print("Fourth Pour:", str(round(pour4,1))+"g")
    print("Begin pour in:")
    countdown(5)
    print("Pour to", str(round(pour1+pour2+pour3+pour4,1))+"g")
    countdown(45)
    clear_terminal()
    print("Finished!")
    return

def recipe3(pour1,pour2,pour3,pour4,pour5):
    print("First Pour:", str(round(pour1,1))+"g")
    print("Begin pour in:")
    countdown(10)
    print("Pour to", str(round(pour1,1))+"g")
    countdown(40)
    clear_terminal()
    print("Second Pour:", str(round(pour2,1))+"g")
    print("Begin pour in:")
    countdown(5)
    print("Pour to", str(round(pour1+pour2,1))+"g")
    countdown(40)
    clear_terminal()
    print("Third Pour:", str(round(pour3,1))+"g")
    print("Begin pour in:")
    countdown(5)
    print("Pour to", str(round(pour1+pour2+pour3,1))+"g")
    countdown(40)
    clear_terminal()
    print("Fourth Pour:", str(round(pour4,1))+"g")
    print("Begin pour in:")
    countdown(5)
    print("Pour to", str(round(pour1+pour2+pour3+pour4,1))+"g")
    countdown(40)
    clear_terminal()
    print("Fifth Pour:", str(round(pour5,1))+"g")
    print("Begin pour in:")
    countdown(5)
    print("Pour to", str(round(pour1+pour2+pour3+pour4+pour5,1))+"g")
    countdown(45)
    clear_terminal()
    print("Finished!")
    return
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
    ratio = input("Please input a coffee to water ratio from 15 to 17: ")
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
total_pour = fourty_pour_init + sixty_pour_init
total_coffee_grams = float(users * grams)

# Asks the user for their Coffee Profile and Strength Preferences
next_step()
print("Would you prefer the flavor profile of your coffee to be acidic, balanced, or sweet?")
first_pour, second_pour = profile(fourty_pour_init)
print("Would you prefer the strength of your coffee's flavor profile to be light, medium, or strong?")
strength_num, third_pour, fourth_pour, fifth_pour = strength(sixty_pour_init)

# Begins recipes
if strength_num == 1 :
    preparations(total_coffee_grams, total_pour)
    recipe1_summary(first_pour,second_pour,third_pour,total_coffee_grams)
    recipe1(first_pour,second_pour,third_pour)
elif strength_num == 2 :
    preparations(total_coffee_grams, total_pour)
    recipe2_summary(first_pour,second_pour,third_pour,fourth_pour,total_coffee_grams)
    recipe2(first_pour,second_pour,third_pour,fourth_pour)
elif strength_num == 3 :
    preparations(total_coffee_grams, total_pour)
    recipe3_summary(first_pour,second_pour,third_pour,fourth_pour,fifth_pour,total_coffee_grams)
    recipe3(first_pour,second_pour,third_pour,fourth_pour,fifth_pour)