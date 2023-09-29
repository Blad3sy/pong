import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, heightScalar, widthScalar):
        super().__init__()

        self.image = pygame.image.load("retro_games/space_invaders/assets/player/player.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1 * heightScalar)
        self.rect = self.image.get_rect(center = pos)
        self.widthScalar = widthScalar
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5 * self.widthScalar
        
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 5 * self.widthScalar
    
    def update(self):
        self.input()