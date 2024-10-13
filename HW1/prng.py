import random as r
import time as t

# import os
# cwd = os.getcwd()
# print(cwd)

assumeGuiOpen = True
# Clears the file 
file1 = open("HW1/pipes/prng-service.txt", "w+")
file1.close()

while assumeGuiOpen:
    t.sleep(1) 
    file1 = open("HW1/pipes/prng-service.txt", "r+")
    text = file1.readlines()
    if len(text) > 0:
        if "Quit" in text[-1]: 
            assumeGuiOpen = False
        if "Run" in text[-1]: 
            randNum = r.randint(1,9999)
            file1 = open("HW1/pipes/prng-service.txt", "w+")
            file1.write(str(randNum))
    file1.close()
    
