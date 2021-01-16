# Tetsu Kasuya's Award Winning 4:6 Recipe 
# version 1.0.2

# Imports
import time
import os
import cursor

# Initializing
user_check = False

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
                    bloom1 = fourty_pour * 0.58
                    bloom2 = fourty_pour * 0.42
                    break
            elif prof_num == 2 :
                    bloom1 = bloom2 = fourty_pour * 0.5
                    break
            elif prof_num == 3 :
                    bloom1 = fourty_pour * 0.42
                    bloom2 = fourty_pour * 0.58
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
        cursor.hide()
        if seconds >= 10 :
            print(str(seconds),end="\r")
            seconds -= 1
            time.sleep(1)
        else :
            print(str(seconds)," ",end="\r")
            seconds -= 1
            time.sleep(1)

def volume_conversion(water) :
    if water >= 1000 :
        water = str(round((water/1000),1)) + "L"
    else :
        water = str(round(water,1)) + "ml"
    return water

def preparations(num_grams,num_water) :
    clear_terminal()
    next_step()
    print("Please prepare", str(round(num_grams,1)),"g of coarsely ground coffee.")
    print("Please prepare", volume_conversion(num_water),"of water at 92 C or 197 F.")
    next_step()
    enter_to_cont()

def rinse(coffee_grams):
    clear_terminal()
    next_step()
    print("PREPARATION:\n- Gather your filter, scale, and your cup of choice.")
    print("- Rinse your filter and pour the", str(round(coffee_grams,1)) + "g", "of coffee grounds into the filter once drained.")
    print("- Discard the water from the filter, put your cup and filter on the scale, shake the filter to level off the coffee grounds, and tare the scale.")
    next_step()

def recipe1_summary(pour1,pour2,pour3,tot_coffee_grams) :
    next_step()
    rinse(tot_coffee_grams)
    print("SUMMARY:\nThere will be a total of three pours, 45 seconds between the start of each pour.\n")
    print("First pour: " + str(round(pour1)) + "g", 
    "\nSecond Pour: " + str(round(pour2)) + "g", 
    "\nThird Pour: " + str(round(pour3)) + "g")
    next_step()
    enter_to_cont()
    clear_terminal()
    return 

def recipe2_summary(pour1,pour2,pour3,pour4,tot_coffee_grams) :
    next_step()
    rinse(tot_coffee_grams)
    print("SUMMARY:\nThere will be a total of four pours, 45 seconds between the start of each pour.\n")
    print("First pour: " + str(round(pour1)) + "g", 
    "\nSecond Pour: " + str(round(pour2)) + "g", 
    "\nThird Pour: " + str(round(pour3)) + "g",
    "\nFourth Pour: " + str(round(pour4)) + "g")
    next_step()
    enter_to_cont()
    clear_terminal()
    return

def recipe3_summary(pour1,pour2,pour3,pour4,pour5,tot_coffee_grams) :
    next_step()
    rinse(tot_coffee_grams)
    print("SUMMARY:\nThere will be a total of five pours, 45 seconds between the start of each pour.\n")
    print("First pour: " + str(round(pour1)) + "g", 
        "\nSecond Pour: " + str(round(pour2)) + "g", 
        "\nThird Pour: " + str(round(pour3)) + "g", 
        "\nFourth Pour: " + str(round(pour4)) + "g", 
        "\nFifth Pour: " + str(round(pour5)) + "g")
    next_step()
    enter_to_cont()
    clear_terminal()
    return

def recipe1(pour1,pour2,pour3):
    #Pour 1
    next_step()
    print("First pour of", str(round(pour1))+"g.\nPour to" , str(round(pour1))+"g.")
    print("Begin pour in:")
    countdown(10)
    clear_terminal()
    next_step()
    print("First pour of", str(round(pour1))+"g.\nPour to" , str(round(pour1))+"g.")
    print("Begin pour!")
    countdown(40)
    clear_terminal()
    #Pour 2
    next_step()
    print("Second pour of", str(round(pour2))+"g.\nPour to" , str(round(pour1+pour2))+"g.")
    print("Begin pour in:")
    countdown(5)
    clear_terminal()
    next_step()
    print("Second pour of", str(round(pour2))+"g.\nPour to" , str(round(pour1+pour2))+"g.")
    print("Begin pour!")
    countdown(40)
    clear_terminal()
    #Pour 3
    next_step()
    print("Third pour of", str(round(pour3))+"g.\nPour to" , str(round(pour1+pour2+pour3))+"g.")
    print("Begin pour in:")
    countdown(5)
    clear_terminal()
    next_step()
    print("Third pour of", str(round(pour3))+"g.\nPour to" , str(round(pour1+pour2+pour3))+"g.")
    print("Begin pour!")
    countdown(45)
    clear_terminal()
    return

def recipe2(pour1,pour2,pour3,pour4):
    #Pour 1
    next_step()
    print("First pour of", str(round(pour1))+"g.\nPour to" , str(round(pour1))+"g.")
    print("Begin pour in:")
    countdown(10)
    clear_terminal()
    next_step()
    print("First pour of", str(round(pour1))+"g.\nPour to" , str(round(pour1))+"g.")
    print("Begin pour!")
    countdown(40)
    clear_terminal()
    #Pour 2
    next_step()
    print("Second pour of", str(round(pour2))+"g.\nPour to" , str(round(pour1+pour2))+"g.")
    print("Begin pour in:")
    countdown(5)
    clear_terminal()
    next_step()
    print("Second pour of", str(round(pour2))+"g.\nPour to" , str(round(pour1+pour2))+"g.")
    print("Begin pour!")
    countdown(40)
    clear_terminal()
    #Pour 3
    next_step()
    print("Third pour of", str(round(pour3))+"g.\nPour to" , str(round(pour1+pour2+pour3))+"g.")
    print("Begin pour in:")
    countdown(5)
    clear_terminal()
    next_step()
    print("Third pour of", str(round(pour3))+"g.\nPour to" , str(round(pour1+pour2+pour3))+"g.")
    print("Begin pour!")
    countdown(40)
    clear_terminal()
    #Pour 4
    next_step()
    print("Fourth pour of", str(round(pour4))+"g.\nPour to" , str(round(pour1+pour2+pour3+pour4))+"g.")
    print("Begin pour in:")
    countdown(5)
    clear_terminal()
    next_step()
    print("Fourth pour of", str(round(pour4))+"g.\nPour to" , str(round(pour1+pour2+pour3+pour4))+"g.")
    print("Begin pour!")
    countdown(45)
    clear_terminal()
    return

def recipe3(pour1,pour2,pour3,pour4,pour5):
 #Pour 1
    next_step()
    print("First pour of", str(round(pour1))+"g.\nPour to" , str(round(pour1))+"g.")
    print("Begin pour in:")
    countdown(10)
    clear_terminal()
    next_step()
    print("First pour of", str(round(pour1))+"g.\nPour to" , str(round(pour1))+"g.")
    print("Begin pour!")
    countdown(40)
    clear_terminal()
    #Pour 2
    next_step()
    print("Second pour of", str(round(pour2))+"g.\nPour to" , str(round(pour1+pour2))+"g.")
    print("Begin pour in:")
    countdown(5)
    clear_terminal()
    next_step()
    print("Second pour of", str(round(pour2))+"g.\nPour to" , str(round(pour1+pour2))+"g.")
    print("Begin pour!")
    countdown(40)
    clear_terminal()
    #Pour 3
    next_step()
    print("Third pour of", str(round(pour3))+"g.\nPour to" , str(round(pour1+pour2+pour3))+"g.")
    print("Begin pour in:")
    countdown(5)
    clear_terminal()
    next_step()
    print("Third pour of", str(round(pour3))+"g.\nPour to" , str(round(pour1+pour2+pour3))+"g.")
    print("Begin pour!")
    countdown(40)
    clear_terminal()
    #Pour 4
    next_step()
    print("Fourth pour of", str(round(pour4))+"g.\nPour to" , str(round(pour1+pour2+pour3+pour4))+"g.")
    print("Begin pour in:")
    countdown(5)
    clear_terminal()
    next_step()
    print("Fourth pour of", str(round(pour4))+"g.\nPour to" , str(round(pour1+pour2+pour3+pour4))+"g.")
    print("Begin pour!")
    countdown(40)
    clear_terminal()
    #Pour 5
    next_step()
    print("Fifth pour of", str(round(pour5))+"g.\nPour to" , str(round(pour1+pour2+pour3+pour4+pour5))+"g.")
    print("Begin pour in:")
    countdown(5)
    clear_terminal()
    next_step()
    print("Fifth pour of", str(round(pour5))+"g.\nPour to" , str(round(pour1+pour2+pour3+pour4+pour5))+"g.")
    print("Begin pour!")
    countdown(45)
    clear_terminal()
    return
###############################

# Main Body
clear_terminal()
print("###########################\nThe 4:6 Pourover Recipe\n###########################\n")
# Checks for # of Consumers
cursor.show()
while user_check == False:
    users = input("Please input the number of coffee consumers: ")
    try:
        users = int(users)
        user_check = True
    except:
        print("Error. Please enter a numerical value.\n")

# Amount of Coffee Grams per user and Ratio
grams = float(20)
ratio = float(15)

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

# Begin recipe
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
print("You're finished pouring! Remove the brewer at 3:30.")
