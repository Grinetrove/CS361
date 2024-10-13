
import pygame as g
import time as t

window = g.display.set_mode((1000,500))
g.display.set_caption('Assignment 1: Microservices Warm-Up')
windowOpen = True

class Button:
    def __init__(self,x,y, image_path, scale = 0.25):
        image = g.image.load(image_path).convert_alpha()
        self.image = g.transform.scale(image,(int(image.get_width()*scale),int(image.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self,window,pressable = False):
        window.blit(self.image, (self.rect.x,self.rect.y))
        if pressable:
            pos = g.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if g.mouse.get_pressed()[0]:
                    file1 = open("HW1/pipes/prng-service.txt", "w+")
                    file1.write("Run\n")
                    file1.close()
                    t.sleep(2)
                    file1 = open("HW1/pipes/prng-service.txt", "r+")
                    file2 = open("HW1/pipes/image-service.txt", "w+")
                    file2.write(str(file1.readlines()[-1]))
                    file1.close()
                    file2.close()

while windowOpen: 
    window.fill((202,228,241))
    startButton = Button(100,50,"HW1/images/Button.png",scale = 0.2)
    startButton.draw(window,pressable=True)
    file2 = open("HW1/pipes/image-service.txt", "r+")
    path = file2.readlines()
    if len(path) > 0 and len(path[0]) > 0:
        if path[0][0] == "H":
            image = Button(500,50,path[0],scale = 0.5) 
            image.draw(window)
    for event in g.event.get():
        if event.type == g.QUIT:
            windowOpen = False
    g.display.update()
g.quit()

t.sleep(3)

file1 = open("HW1/pipes/prng-service.txt", "w+")
file1.write("Quit\n")
file1.close()
file2 = open("HW1/pipes/image-service.txt", "w+")
file2.write("Quit\n")
file2.close()
