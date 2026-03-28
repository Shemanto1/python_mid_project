import pygame
import random

size = 40

class Apple:
    def __init__(self,parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.a =size*3
        self.b =size*3

    def draw(self):

        self.parent_screen.blit(self.image,(self.a,self.b))
        pygame.display.update()

    def move(self):
        self.a = random.randint(0,24)*size
        self.b = random.randint(0,19)*size