# This is the main page for all of the recipes!
import FourtySixty
import Hoffman

question = "\nPlease enter 1 or 2 to determine the coffee recipe:\n\n 1. 4:6 Method\n 2. Hoffman\n\nEnter here: "
rec_num = False
while rec_num not in [1, 2] :
    rec_num = input(question)
    try :
        rec_num = int(str_num)
        if rec_num == 1 :
                FourtySixty()
                break
        elif rec_num == 2 :
                Hoffman()
                break
        else :
            print("\nError.")
    except :
            print("\nError.")