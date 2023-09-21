import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("retro_games/space_invaders/assets/player/player.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        self.rect = self.image.get_rect(center = pos)
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 5
    
    def update(self):
        self.input()