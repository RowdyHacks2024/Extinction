import pygame
from pygame.locals import *
import random

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("orange-square.png")
        self.rect = self.image.get_rect()
        self.rect.center=(400,400)

    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30,370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("blue-square.png")
        self.rect = self.image.get_rect()
        self.rect.center=(600,200)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < 1280:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)


    def draw(self, surface):
        surface.blit(self.image, self.rect)
            
