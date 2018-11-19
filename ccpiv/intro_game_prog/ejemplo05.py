import pygame
import sys
from pygame.locals import *

WIDTH = 480
HEIGHT = 320

speed = 8
maloso_speed = 4

x = 50
y = 260

prota_w = 50
prota_h = 37
prota_vidas = 3
prota_tocado = False
prota_tiempo = 0

prota_flipped = False

maloso_x = WIDTH - 100
maloso_y = 242
maloso_vivo = True
maloso_vidas = 3

floor_y = 260

jump_h = 80
jump_speed = -4

jump_speed_up = -4
jump_speed_down = 2

jumping = False

bullet_x = x
bullet_y = y
bullet_speed = 8
bullet_dir = 1
bullet_flipped = False

fire = False



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Intro Programación Juegos')
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

prota = pygame.image.load("adventurer-idle-00.png")
bg = pygame.image.load("background.jpg")
maloso = pygame.image.load("maloso.png")
bullet = pygame.image.load("proyectil.gif")


bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
maloso = pygame.transform.scale(maloso, (64, 64))
bullet = pygame.transform.scale(bullet, (48, 48))



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
    
    #si llegamos al tope, bajamos
    if y <= floor_y - jump_h:
        y = floor_y - jump_h
        jump_speed = jump_speed_down
    
    #si llegamos al suelo, reiniciamos valores
    if y >= floor_y:
        y = floor_y
        jump_speed = jump_speed_up
        jumping = False
    
    
def maloso_mov ():
    global maloso_x
    global maloso_speed
    global prota_tocado
    
    maloso_x = maloso_x - maloso_speed
    
    if maloso_x <= 0:
        maloso_x = 0
        maloso_speed = -maloso_speed
    
    if maloso_x >= WIDTH - 64:
        maloso_x = WIDTH - 64
        maloso_speed = -maloso_speed
        
    if not prota_tocado:
        if (x >= maloso_x and x <= maloso_x + 64) or (x + 48 >= maloso_x and x + 48 <= maloso_x + 64):
            if (y >= maloso_y and y <= maloso_y + 64) or (y + 48 >= maloso_y and y + 48 <= maloso_y + 64):
                print('GOLPE')
                prota_tocado = True
    
def bullet_mov ():
    global bullet_x
    global bullet_y
    global fire
    global maloso_vivo
    global maloso_vidas
    global maloso_x
        
    bullet_x = bullet_x + bullet_dir*bullet_speed
    
    if bullet_x <= 0:
        fire = False
    elif bullet_x >= WIDTH:
        fire = False
    
    if maloso_vivo:
        if (bullet_x >= maloso_x and bullet_x <= maloso_x + 64) or (bullet_x + 48 >= maloso_x and bullet_x + 48 <= maloso_x + 64):
            if (bullet_y >= maloso_y and bullet_y <= maloso_y + 64) or (bullet_y + 48 >= maloso_y and bullet_y + 48 <= maloso_y + 64):
                fire = False
                maloso_vidas = maloso_vidas - 1
                maloso_x = WIDTH - 200
                                
                if maloso_vidas <= 0:
                    maloso_vivo = False

        
    
if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                
        keys=pygame.key.get_pressed()
        if keys[K_LEFT]:
            print("Izquierda")
            if not prota_flipped:
                prota_flipped = True
                prota = pygame.transform.flip(prota, True, False)
            x = x - speed
            if x <= 0:
                x = 0
                
        if keys[K_RIGHT]:
            print("Derecha")
            if prota_flipped:
                prota_flipped = False
                prota = pygame.transform.flip(prota, True, False)
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
        
        if keys[K_f]:
            if not fire:
                fire = True
                bullet_x = x
                bullet_y = y
                
                bullet_dir = 1
                
                if prota_flipped:
                    bullet_dir = -1
                    if not bullet_flipped:
                        bullet = pygame.transform.flip(bullet, True, False)
                        bullet_flipped = True
                else:
                    if bullet_flipped:
                        bullet = pygame.transform.flip(bullet, True, False)
                        bullet_flipped = False
            
        saltando()
        

        color = [0, 0, 0]
        screen.fill(color)
        
        screen.blit(bg, (0,0))
        
        if not prota_tocado:
            screen.blit(prota, (x, y))
        else:
            prota_tiempo = prota_tiempo + 1
            fire = False
            if prota_tiempo % 2 == 0:
                screen.blit(prota, (x, y))
            
            if prota_tiempo >= 120:
                prota_tocado = False

        
        if maloso_vivo:
            maloso_mov()
            screen.blit(maloso, (maloso_x, maloso_y))
        
        if fire:
            bullet_mov()
            screen.blit(bullet, (bullet_x, bullet_y))
            
        pygame.display.flip()
        clock.tick(30)
