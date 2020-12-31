import time
import os

def clear_terminal() :
    os.system('cls' if os.name == 'nt' else 'clear')

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
    print("Finished")
    return


clear_terminal()
recipe1(15,15,15)