import numpy as np
import pygame 
import math


velocita= 10
#g= 6.674 * pow(10, -11)
g = 1
dt=0.01
posizione1= [750, 500]
posizione2= [600,400]
pygame.init()
screen = pygame.display.set_mode((1500, 1000))
vettore1= pygame.Vector2(posizione1)
vettore2=pygame.Vector2(posizione2)
clock = pygame.time.Clock() 
running = True 

font=pygame.font.SysFont(None, 30)

raggio1=30
raggio2=5

massa1=raggio1*10
massa2=raggio2*10
velocita2= pygame.Vector2(0,1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.circle(screen, "black", vettore1, raggio1)
    pygame.draw.circle(screen, "black", vettore2, raggio2)
    vettorer= vettore1-vettore2 #vettore che va da 2 a 1
    r_normalizzato=vettorer.normalize()
    distance = math.sqrt(pow(vettore1.x - vettore2.x, 2)+ pow(vettore1.y - vettore2.y, 2))
    
    force = g * ((massa1 *massa2)/ pow(distance, 2)) #forza gravitazione
    force_vector= force * r_normalizzato #forza vettoriale
    
    acceleration2 = force_vector / massa2 #accelerazione del corpo 2
    
    velocita2 += acceleration2 * dt
    vettore2 += velocita2 * dt

    text1 = font.render("Distanza: "  + str(round(distance, 2)), True, "black")
    text2 = font.render("Costante di gravità: " + str(g), True , "black")
    text3 = font.render("Forza  = " + str(round(force, 2)), True,  "black")
    text4 = font.render("Accelerazione = " + str(round(acceleration2, 2)), True, "black")
    screen.blit(text1, (10, 20))
    screen.blit(text2, (10, 40))
    screen.blit(text3, (10, 60))
    screen.blit(text4, (10, 80))
    pygame.display.flip()
    clock.tick(60) 
    

pygame.quit()
