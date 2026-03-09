import numpy as np
import pygame 
import math


velocita= 10
# g= 6.674 * pow(10, -11)
g = 1
dt=0.1
posizione1= [750, 500]
posizione2= [600,400]
pygame.init()
screen = pygame.display.set_mode((1500, 1000))
vettore1= pygame.Vector2(posizione1)
vettore2=pygame.Vector2(posizione2)
vettorer= pygame.Vector2((posizione1[0]-posizione2[0]), posizione1[1]-posizione2[1])
clock = pygame.time.Clock() 
running = True 

font=pygame.font.SysFont(None, 30)

raggio1=30
raggio2=5

massa1=raggio1*10
massa2=raggio2*10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.circle(screen, "black", vettore1, raggio1)
    pygame.draw.circle(screen, "black", vettore2, raggio2)
    distance = math.sqrt(pow(vettore1.x - vettore2.x, 2)+ pow(vettore1.y - vettore2.y, 2))
    force = g * ((massa1 *massa2)/ pow(distance, 2))
    acceleration2 = force / massa2
    text1 = font.render("Distanza: "  + str(round(distance, 2)), True, "black")
    text2 = font.render("Costante di gravità: " + str(g), True , "black")
    text3 = font.render("Forza  = " + str(force), True,  "black")
    text4 = font.render("Accelerazione = " + str(acceleration2), True, "black")
    screen.blit(text1, (10, 20))
    screen.blit(text2, (10, 40))
    screen.blit(text3, (10, 60))
    screen.blit(text4, (10, 80))
    pygame.display.flip()
    clock.tick(60) 
    

pygame.quit()
