import pygame
import os
import time
from pygame.locals import *

class Game:
    def __init__(self):
        self.running = False
        
        self.width = 500
        self.height = 500
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.renderables = [] #renderable is something that has render() function
        self.logicals = [] #logical is something that has update() function
        self.eventhandlers = [] #has function handle(event from pygame.event.get())
        
        pygame.display.set_caption("Happy new year 2016! :D")

    
    def run(self):
        self.running = True
        while (self.running):
            self.logic()
            self.render()

    
    def logic(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            for eventhandler in self.eventhandlers:
                eventhandler.handle(event)

        for logical in self.logicals:
            logical.update()

    
    def render(self):
        self.screen.fill((100,254,110))
        for renderable in self.renderables:
            renderable.render()
        pygame.display.flip();

    
    def set_height(self, height):
        self.height = height

    
    def set_width(self, width):
        self.width = width


def main():
    pygame.init()
    game = Game()
    game.run()

main()