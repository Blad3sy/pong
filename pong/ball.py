import pygame
from random import randint, choice

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("retro_games/pong/assets/ball.png")
        self.rect = self.image.get_rect(center = (500, 0))

        self.exponents = [-1, 1]
        self.xMovement = 5 * choice(self.exponents)
        self.yMovement = 5 * choice(self.exponents)

        self.rect.y = randint(50, 550)
    
    def movement(self):
        self.rect.x += self.xMovement
        self.rect.y -= self.yMovement

        if self.rect.y >= 600 or self.rect.y <= 0:
            self.yMovement *= -1
        
        if self.rect.x >= 1100 or self.rect.x <= -100:
            self.reset()
    
    def reset(self):
        self.xMovement = 5 * choice(self.exponents)
        self.yMovement = 5 * choice(self.exponents)
        self.rect.x = 500
        self.rect.y = randint(50, 550)

    def update(self):
        self.movement()