import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Extinction")

from characters import Meteor
from characters import Dinosaur

screen.fill("red")

player = Meteor()
enemy = Dinosaur()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("red")

    # RENDER YOUR GAME HERE
    player.update()
    enemy.move()

    player.draw(screen)
    enemy.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
