import pygame
from pygame.locals import *
import random

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("orange-square.png")
        self.rect = self.image.get_rect()
        self.rect.center=(360,720)
        self.move_right = True

    def move(self):

        if (self.rect.right > 1280 or self.rect.left < 0):
            if(self.move_right == True):
                self.move_right = False
                self.rect.right = 1280
            else:
                self.move_right = True
                self.rect.left = 0

        else:
            if (self.move_right == True):
                self.rect.move_ip(3, 0)
            else:
                self.rect.move_ip(-3, 0)
            if (random.randint(0, 50) == 0):
                if (self.move_right == True):
                    self.move_right = False
                else:
                    self.move_right = True
 #       if (self.rect.bottom > 600):
 #           self.rect.top = 0
 #           self.rect.center = (random.randint(30,370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("blue-square.png")
        self.rect = self.image.get_rect()
        self.rect.center=(600,200)

    def update(self):

        self.rect.move_ip(0, 5)
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < 1280:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)

        if self.rect.bottom > 720:
            self.rect.center=(640, -300)


    def draw(self, surface):
        surface.blit(self.image, self.rect)
            
