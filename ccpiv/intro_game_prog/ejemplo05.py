import pygame
import sys
from pygame.locals import *

WIDTH = 480
HEIGHT = 320

speed = 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Intro Programación Juegos')
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

prota = pygame.image.load("adventurer-idle-00.png")
bg = pygame.image.load("background.jpg")

bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))


if __name__ == "__main__":
    x = 50
    y = 260
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
            
        color = [0, 0, 0]
        screen.fill(color)
        
        screen.blit(bg, (0,0))
        screen.blit(prota, (x, y))

        
        pygame.display.flip()
        clock.tick(60)
