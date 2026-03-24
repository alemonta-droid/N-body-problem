import numpy as np
import pygame 
import math


velocita= 10
#g= 6.674 * pow(10, -11)
g = 0.1
dt=0.5
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
raggio3=5

massa1=raggio1*100
massa2=raggio2*1000
massa3=raggio3*100

velocita1=pygame.Vector2(0,0)
velocita2= pygame.Vector2(0,1)
velocita3=pygame.Vector2(0,-1)

acceleration1=pygame.Vector2(0,0)
acceleration2=pygame.Vector2(0,0)

def predici_orbita(pos, vel, passi):
    pos_temp = pos.copy()
    vel_temp = vel.copy()
    punti = []

    for i in range(passi):

        r = vettore1 - pos_temp
        distance = r.length()

        if distance < 5:
            distance = 5

        r_unit = r.normalize()

        force = g * massa1 * massa2 / distance**2
        force_vector = r_unit * force

        acc = force_vector / massa2

        vel_temp += acc * dt
        pos_temp += vel_temp * dt

        punti.append((pos_temp.x, pos_temp.y))

    return punti

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
            
    screen.fill("white")
    pygame.draw.circle(screen, "black", vettore1, raggio1)
    pygame.draw.circle(screen, "black", vettore2, raggio2)
    vettorer1= vettore1-vettore2 #vettore che va da 2 a 1
    vettorer2= vettore2-vettore1 #vettore che va da 1 a 2
    r1_normalizzato=vettorer1.normalize()
    r2_normalizzato=vettorer2.normalize()
    
    distance = math.sqrt(pow(vettore1.x - vettore2.x, 2)+ pow(vettore1.y - vettore2.y, 2))
    
    force = g * ((massa1 *massa2)/ pow(distance, 2)) #forza gravitazione
    
    force_vector1= force * r2_normalizzato #forza vettoriale corpo 1
    force_vector2= force * r1_normalizzato #forza vettoriale corpo 2
    
    acceleration1_vecchia= acceleration1 #salva la vecchia accelereazione per Verlet
    acceleration2_vecchia= acceleration2 
    
    
    orbita_prevista = predici_orbita(vettore2, velocita2, 3500)
    if len(orbita_prevista) > 1:
        pygame.draw.lines(screen, "lightblue", False, orbita_prevista,1)
    
    velocita_n=math.sqrt(pow(velocita2.x, 2) + pow(velocita2.y, 2))
    
    vettore1 = vettore1 + velocita1 * dt + 1/2 * acceleration1 * pow(dt, 2) # Formula di Verlet
    vettore2 = vettore2 + velocita2 * dt + 1/2 * acceleration2 * pow(dt, 2) # Formula di Verlet
    
    xcm= (massa1*vettore1.x + massa2*vettore2.x)/ (massa1+massa2) #centri di massa
    ycm= (massa1*vettore1.y + massa2*vettore2.y)/ (massa1+massa2)
    
    vettorem= pygame.Vector2(xcm, ycm)
    
    pygame.draw.circle(screen, "red", vettorem, raggio2)
    
    acceleration1 = force_vector1 / massa1 #accelerazione del corpo 1
    acceleration2 = force_vector2 / massa2 #accelerazione del corpo 2
    
    velocita1 += ((acceleration1 + acceleration1_vecchia)/2) * dt
    velocita2 += ((acceleration2 + acceleration2_vecchia)/2)*dt
    
    velocita_fuga=math.sqrt(2*g *massa1/distance)

    if (distance <= raggio1+raggio2):
        running=False
    
    
    text1 = font.render("Distanza: "  + str(round(distance, 2)), True, "black")
    text2 = font.render("Costante di gravità: " + str(g), True , "black")
    text3 = font.render("Forza  = " + str(round(force, 2)), True,  "black")
    text4 = font.render("Velocità = " + str(round(velocita_n, 2)), True, "black")
    text5 = font.render("Velocità di fuga = " + str(round(velocita_fuga, 2)), True,  "black")
    
    screen.blit(text1, (10, 20))
    screen.blit(text2, (10, 40))
    screen.blit(text3, (10, 60))
    screen.blit(text4, (10, 80))
    screen.blit(text5, (10, 100))
    pygame.display.flip()
    clock.tick(60) 
    

pygame.quit()
