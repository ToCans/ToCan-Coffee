fourty_pour_init = 40

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

print("Would you prefer the profile of your coffee to be bitter, sweet, or balanced?\n")
first_bloom,second_bloom = profile(fourty_pour_init)
print(first_bloom,second_bloom)

