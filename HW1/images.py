import random as r
import time as t

# import os
# cwd = os.getcwd()
# print(cwd)

assumeGuiOpen = True
# Clears the file 
file1 = open("HW1/pipes/image-service.txt", "w+")
file1.close()

while assumeGuiOpen:
    t.sleep(1) 
    file1 = open("HW1/pipes/image-service.txt", "r+")
    text = file1.readlines()
    if len(text) > 0:
        if "Quit" in text[-1]: 
            assumeGuiOpen = False
        try:
            randNum = int(text[-1]) % 8 + 1
            print(randNum)
            file1 = open("HW1/pipes/image-service.txt", "w+")
            file1.write("HW1/images/Meme"+str(randNum)+".png")
        except:
            assert(0==0)
    file1.close()
    
