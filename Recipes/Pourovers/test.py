# Tetsu Kasuya's Award Winning 4:6 Recipe 
# version 1.0.2
# Script by u/ToCans

# Imports
import time
import os
import cursor
import sys
import threading

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
    return

# Working Stop Watch
#def stopwatch(stop_minute, stop_second, end_min, end_second) :
   #global stop_minute
   #global stop_second
    #cursor.hide()
    #while stop_second < 60 :
        #if stop_minute == end_min and stop_second == end_second :
            #print(str(stop_minute)+":"+str(stop_second))
            #break
        #if stop_second < 10 :
            #stopwatch_output = str(stop_minute)+":0"+str(stop_second)
            #print(stopwatch_output,end="\r")
            
        #else :
            #stopwatch_output = str(stop_minute)+":"+str(stop_second)
            #print(stopwatch_output,end="\r")
        #stop_second += 1
        #time.sleep(1)
        #if stop_second == 60 :
            #stop_minute += 1
            #stop_second = 0
    #cursor.show()
    #return stop_minute, stop_second

# Experimental Stop Watch
def stopwatch(stop_minute, stop_second, end_min, end_second) :
   #global stop_minute
   #global stop_second
    cursor.hide()
    while stop_second < 60 :
        if stop_minute == end_min and stop_second == end_second :
            print(str(stop_minute)+":"+str(stop_second))
            break
        if stop_second < 10 :
            stopwatch_output = str(stop_minute)+":0"+str(stop_second)
            print(stopwatch_output,end="\r")  
        else :
            stopwatch_output = str(stop_minute)+":"+str(stop_second)
            print(stopwatch_output,end="\r")
        stop_second += 1
        time.sleep(1)
        if stop_second == 60 :
            stop_minute += 1
            stop_second = 0
    cursor.show()
    return stop_minute, stop_second

def recipe1(pour1,pour2,pour3):
    #Pour 1
    next_step()
    print("First pour of", str(round(pour1))+"g.\nPour to" , str(round(pour1))+"g.")
    print("Begin pour in:")
    stopwatch(0, 0, 3, 30)
    #countdown(10)
    clear_terminal()
    next_step()
    print("First pour of", str(round(pour1))+"g.\nPour to" , str(round(pour1))+"g.")
    print("Begin pour!")
    #countdown(10)
    clear_terminal()
    #Bloom
    next_step()
    print("Let the coffee bloom for:")
    #countdown(15)
    clear_terminal()
    #Pour 2
    next_step()
    print("Second pour of", str(round(pour2))+"g.\nPour to" , str(round(pour1+pour2))+"g.")
    print("Begin pour in:")
    #countdown(5)
    clear_terminal()
    next_step()
    print("Second pour of", str(round(pour2))+"g.\nPour to" , str(round(pour1+pour2))+"g.")
    print("Begin pour!")
    #countdown(40)
    clear_terminal()
    #Pour 3
    next_step()
    print("Third pour of", str(round(pour3))+"g.\nPour to" , str(round(pour1+pour2+pour3))+"g.")
    print("Begin pour in:")
    #countdown(5)
    clear_terminal()
    next_step()
    print("Third pour of", str(round(pour3))+"g.\nPour to" , str(round(pour1+pour2+pour3))+"g.")
    print("Begin pour!")
    #countdown(30)
    clear_terminal()
    return

#Main
# Playing around with threading
clear_terminal()
t1 = threading.Thread(target=stopwatch,args=(0,0,0,15))
print("Stopwatch:")
t1.start()