import pygame
import sys
from pygame.locals import *



pygame.init()
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption('Intro Progr. Juegos')
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

image = pygame.image.load("adventurer-idle-00.png")


if __name__ == "__main__":
    while True:
        screen.blit(image, (50, 100))
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        clock.tick(60)
