import pygame
from math import floor

class Shield(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        sh1 = pygame.image.load("retro_games/space_invaders/assets/shield/shield1.png")
        sh2 = pygame.image.load("retro_games/space_invaders/assets/shield/shield2.png")
        sh3 = pygame.image.load("retro_games/space_invaders/assets/shield/shield3.png")
        sh4 = pygame.image.load("retro_games/space_invaders/assets/shield/shield4.png")
        sh5 = pygame.image.load("retro_games/space_invaders/assets/shield/shield5.png")
        sh6 = pygame.image.load("retro_games/space_invaders/assets/shield/shield6.png")

        self.frames = [sh1, sh2, sh3, sh4, sh5, sh6]
        self.state = 0

        self.image = self.frames[self.state]
        self.image = pygame.transform.scale(self.image, (72, 56))
        self.rect = self.image.get_rect(center = pos)
    
    def nextState(self):
        self.state += 0.4
        if self.state >= 6:
            self.kill()
        else:
            self.image = self.frames[floor(self.state)]
            self.image = pygame.transform.scale(self.image, (72, 56))