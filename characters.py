import pygame
from pygame.locals import *
import random

class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("exp.PNG")
        self.rect = self.image.get_rect()

    #draw (important probably)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def drawGround(self, surface,x):
        self.rect.center=(x, 720)
        surface.blit(self.image, self.rect)


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dino.PNG")
        self.rect = self.image.get_rect()
        self.rect.center=(360,720)  #spawn in the middle
        self.rect.bottom=(720)
        self.move_right = True      #move right initially

    def move(self):

        #if dinosaur hits the bounds of the window
        if (self.rect.right > 1280 or self.rect.left < 0):
            #invert movement and place the dinosaur back in bounds
            if(self.move_right == True):    
                self.move_right = False
                self.rect.right = 1280
            else:
                self.move_right = True
                self.rect.left = 0

        #if dinosaur is within bounds
        else:
            #move according to previously set direction
            if (self.move_right == True):
                self.rect.move_ip(3, 0)
            else:
                self.rect.move_ip(-3, 0)

            #randomly change movement direction
            if (random.randint(0, 50) == 0):
                if (self.move_right == True):
                    self.move_right = False
                else:
                    self.move_right = True
            
    #draw (important probably)
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("met1.PNG")
        self.rect = self.image.get_rect()
        self.rect.center=(600,200)

    def update(self):

        self.rect.move_ip(0, 5)
        pressed_keys = pygame.key.get_pressed()
        #print(self.rect.collidepoint(pygame.mouse.get_pos()));
        
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
            
