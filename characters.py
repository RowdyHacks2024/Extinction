

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("orange-square.png")
        self.rect = pygame.image.get_rect()
        self.rect.center=(400,400)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Meteor(pygame.sprite.Sprite)
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("blue-square.png")
        self.rect = pygame.image.get_rect()
        self.rect.center=(600,200)

    def draw(self, surface)
        surface.blit(self.image, self.rect)
            
