# James Hoffman's Ultimate V60 Recipe
# version 1.0.0

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

def rinse(coffee_grams):
    clear_terminal()
    next_step()
    print("PREPARATION:\n- Gather your filter, scale, and your cup of choice.")
    print("- Rinse your filter and pour the", str(round(coffee_grams,1)) + "g", "of coffee grounds into the filter once drained.")
    print("- Discard the water from the filter, put your cup and filter on the scale, shake the filter to level off the coffee grounds, and tare the scale.")
    next_step()

def preparations(num_grams,num_water) :
    clear_terminal()
    next_step()
    print("Please prepare", str(round(num_grams,1)),"g of medium to fine ground coffee.")
    print("Please prepare", volume_conversion(num_water),"of water at 98 C or 209 F.")
    next_step()
    enter_to_cont()

def volume_conversion(water) :
    if water >= 1000 :
        water = str(round((water/1000),1)) + "L"
    else :
        water = str(round(water,1)) + "ml"
    return water

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
    cursor.show()

def recipe1_summary(pour1,pour2,pour3,tot_coffee_grams) :
    next_step()
    rinse(tot_coffee_grams)
    print("SUMMARY:\nThere will be a total of three pours:\n")
    print("First pour: " + str(round(pour1)) + "g", 
    "\nSecond Pour: " + str(round(pour2)) + "g", 
    "\nThird Pour: " + str(round(pour3)) + "g")
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
    countdown(10)
    clear_terminal()
    #Bloom
    next_step()
    print("Let the coffee bloom for:")
    countdown(15)
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
    countdown(30)
    clear_terminal()
    return

###############################
# Main Body
clear_terminal()
print("###########################\nThe Hoffman V60 Recipe\n###########################\n")
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
grams = float(15)
ratio = float(16.667)

# Calculaltions
sixty_pour_init = float(users * grams * ratio * 0.6)
fourty_pour_init = float(users * grams * ratio * 0.4)
total_pour = fourty_pour_init + sixty_pour_init
total_coffee_grams = float(users * grams)
bloom = float(users * grams * 2)
main_pour = sixty_pour_init - bloom

# Begin Recipe
preparations(total_coffee_grams, total_pour)
recipe1_summary(bloom,main_pour,fourty_pour_init,total_coffee_grams)
recipe1(bloom,main_pour,fourty_pour_init)
print("You're finished pouring! Remove the brewer at 3:00.")
