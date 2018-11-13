import pygame
import sys
from pygame.locals import *

WIDTH = 480
HEIGHT = 320

speed = 8

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Intro Programación Juegos')
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

prota = pygame.image.load("adventurer-idle-00.png")
bg = pygame.image.load("background.jpg")
maloso = pygame.image.load("maloso.png")

bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

x = 50
y = 260

floor_y = 260

jump_h = 50
jump_speed = -4

jumping = False

def salto ():
    global y
    global jumping
    
    if not jumping:
        #y = y - 50
        #if y <= 0:
        #    y = 0
        jumping = True
        
def saltando ():
    global y
    global jumping
    global jump_speed
    global floor_y
    global jump_h
    
    if not jumping:
        return
    
    y = y + jump_speed
    
    if y <= floor_y - jump_h:
        y = floor_y - jump_h
        jump_speed = -jump_speed
        
    if y >= floor_y:
        y = floor_y
        jump_speed = -jump_speed
        jumping = False
    
    


if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                
        keys=pygame.key.get_pressed()
        if keys[K_LEFT]:
            print("Izquierda")
            x = x - speed
            if x <= 0:
                x = 0
                
        if keys[K_RIGHT]:
            print("Derecha")
            x = x + speed
            if x >= WIDTH - 50:
                x = WIDTH - 50
                
        #"""                
        if keys[K_UP]:
            print("Arriba")
            y = y - speed
            if y <= 0:
                y = 0
                
        if keys[K_DOWN]:
            print("Abajo")
            y = y + speed
            if y >= HEIGHT - 37:
                y = HEIGHT - 37       
        #"""
                
        if keys[K_SPACE]:
            salto()
            
        saltando()

        color = [0, 0, 0]
        screen.fill(color)
        
        screen.blit(bg, (0,0))
        screen.blit(prota, (x, y))
        
        screen.blit(maloso, (WIDTH -100, y))

        
        pygame.display.flip()
        clock.tick(30)
