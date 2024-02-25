import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Extinction")

from characters import * 
#from characters import Dinosaur


white = (255, 255, 255)
player = Meteor()
enemys = [Dinosaur(), Dinosaur()]
expl = Explosion()
playerPosX = 0;
playerPosY = 0;
num = 0
bg = pygame.image.load("jurassic.png");
freeze = 0
explosion = pygame.image.load("exp.PNG")
explosion_x = 0
explosion_y = 0
FONT = pygame.font.SysFont("freesansbold", 100)

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
    text = FONT.render(str(num), True, white)
    textRect =  text.get_rect()
    textRect.center = (400//2, 400//2)
    screen.blit(text, textRect)


    # RENDER GAME HERE
    for i in enemys:
        
        if player.rect.colliderect(i.rect):
            player.image = pygame.image.load("met1.PNG")
            player.image.get_rect()
            explosion_x = player.rect.x
            explosion_y = player.rect.y
            player.rect.center=(360, 0)
            expl.rect.center=(explosion_x, 720);
            print("Hit")
            freeze = 60 

            num += 1

            print(num)


    if player.rect.bottom >= 720:
        playerPosX = player.rect.x
        playerPosY = player.rect.y

    if player.rect.collidepoint(playerPosX, playerPosY):
        expl.drawGround(screen, playerPosX)
        freeze = 60

#    if expl.rect.colliderect(enemy.rect):
#        print("hit")
#        num += 1
#        print(num)



    
    if freeze > 0:
        freeze -= 1
        expl.draw(screen)

    player.update()
    #print("enemy: " + str(enemy.rect.top));

    for i in enemys:
        i.move()
        i.draw(screen)

    player.draw(screen)

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
