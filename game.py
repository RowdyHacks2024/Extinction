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
enemys = []
for i in range(7):
    enemys.append(Dinosaur())
expl = Explosion()
playerPosX = 0;
playerPosY = 0;
num = 0
bg = pygame.image.load("./jurassic.png");
freeze = 0
explosion = pygame.image.load("./exp.PNG")
explosion_x = 0
explosion_y = 0
FONT = pygame.font.SysFont("freesansbold", 100)
explode = False
stage = 1
score = False

#explosion = pygame.sprite.Sprite()
#explosion.rect = pygame.image.get_rect(explosion.image)
#print(explosion1.get_rect())

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #stage change when all dinosaurs killed
    if len(enemys) == 0:
        stage = 2
        enemys = []
        for i in range(7):
            enemys.append(EnemyMeteor())
        player = PlayerDinosaur()


    #PLAY AS METEOR
    if stage == 1:

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
                #player.image = pygame.image.load("./met1.PNG")
                #player.image.get_rect()
                explosion_x = player.rect.x
                explosion_y = player.rect.y
                player.rect.center=(360, 0)
                expl.rect.center=(explosion_x, 720);
                print("Hit")
                explode = True
                #freeze = 60 

                #num += 1

                #print(num)


        if player.rect.bottom >= 720:
            playerPosX = player.rect.x
            playerPosY = player.rect.y

        #draw explosion object when hitting the ground
        if player.rect.collidepoint(playerPosX, playerPosY):
            expl.drawGround(screen, playerPosX)
            #freeze = 60
            explode = True
            print("ground collision")

        if explode == True:
            for i in enemys: 
                if expl.rect.colliderect(i.rect):
                    print("hit")
                    num += 1
                    print(num)
                    enemys.remove(i)
            freeze = 60
            explode = False 



        
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


    #PLAY AS DINOSAUR
    elif stage == 2:
        # fill the screen with a color to wipe away anything from last frame

        #screen.fill("red")
        screen.blit(bg,(0, 0))
        text = FONT.render(str(num), True, white)
        textRect =  text.get_rect()
        textRect.center = (400//2, 400//2)
        screen.blit(text, textRect)


        # RENDER GAME HERE
        score = False
        for i in enemys:
            
            if player.rect.colliderect(i.rect):
                #player.image = pygame.image.load("./met1.PNG")
                #player.image.get_rect()
                explosion_x = i.rect.x
                explosion_y = i.rect.y
                player.rect.center=(-300, -300)
                expl.rect.center=(explosion_x, 720);
                #print("Player got Hit")
                explode = True
                #freeze = 60 

            if i.rect.bottom >= 720:
                playerPosX = i.rect.x
                playerPosY = i.rect.y
                #num += 1

            #draw explosion object when hitting the ground
            if i.rect.collidepoint(playerPosX, playerPosY):
                #freeze = 60
                
                print("ground collision")
                expl.drawGround(screen, playerPosX)
                score = True

        if explode == True:
            score = False
            expl.drawGround(screen, playerPosX)
            print("Player got Hit")

            player = ""
            running = False
            freeze = 60
            explode = False 

        if score == True:
            num += 1



        
        if freeze > 0:
            freeze -= 1
            expl.draw(screen)

        if player != "":
            player.update()
        #print("enemy: " + str(enemy.rect.top));

        for i in enemys:
            i.move()
            i.draw(screen)

        if player != "":
            player.draw(screen)

        

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

for i in range(60):
    clock.tick(60)
pygame.quit()
