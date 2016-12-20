import pygame
import os
import time
from pygame.locals import *

def main():
    HEIGHT = 500
    WIDTH = 400

    pygame.init()
    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption("Happy new year 2016! :D")

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

main()