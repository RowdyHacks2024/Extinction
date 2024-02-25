import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Extinction")

from characters import Meteor
from characters import Dinosaur

player = Meteor()
enemy = Dinosaur()
num = 0
bg = pygame.image.load("jurassic.png");
freeze = 0
explosion = pygame.image.load("exp.PNG")
explosion_x = 0
explosion_y = 0
#explosion = pygame.sprite.Sprite()
#explosion.rect = pygame.image.get_rect(explosion.image)
#print(explosion1.get_rect())

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    #screen.fill("red")
    screen.blit(bg,(0, 0))


    # RENDER YOUR GAME HERE
    if player.rect.colliderect(enemy.rect):
        player.image = pygame.image.load("met1.PNG")
        player.image.get_rect()
        explosion_x = player.rect.centerx - 64
        explosion_y = player.rect.centery - 64
        player.rect.center=(360, -300)
        #explosion1.rect.center=(player.rect.center)
        freeze = 60

        num += 1
        print(num)

    
    if freeze > 0:
        freeze -= 1
        screen.blit(explosion,(explosion_x, explosion_y))
    else:
        player.update()
    #print("player:" + str(player.rect.bottom));
    #print("enemy: " + str(enemy.rect.top));

    enemy.move()

    

    player.draw(screen)
    enemy.draw(screen)

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
