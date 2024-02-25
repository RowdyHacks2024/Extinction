import pygame

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

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("red")

    # RENDER YOUR GAME HERE
    if player.rect.colliderect(enemy.rect):
        player.rect.center=(360, -300)
        num += 1
        print(num)



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
