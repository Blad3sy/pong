import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self, startX, startY):
        super().__init__()

        image1 = pygame.image.load("retro_games/space_invaders/assets/enemy/enemy.png")
        image1 = pygame.transform.scale(image1, (33, 24))

        image2 = pygame.image.load("retro_games/space_invaders/assets/enemy/enemyMove.png")
        image2 = pygame.transform.scale(image2, (33, 24))

        self.frames = [image1, image2]
        self.aniIndex = 0

        self.image = self.frames[self.aniIndex]
        self.rect = self.image.get_rect(center = (startX, startY))

        self.movementVal = 8
        self.movementCooldownBase = 80
        self.movementCooldown = 80
        self.speedup = 400
        self.randomUpperLimit = 1000
        self.drop = False
        self.bulletSpeed = 15
    
    def movement(self):
        if self.movementCooldown <= 0:
            self.movementCooldown = self.movementCooldownBase
            self.rect.x += self.movementVal
            if self.drop: 
                self.rect.y += 20
                self.drop = False

            self.aniIndex += 1
            if self.aniIndex > 1: self.aniIndex = 0
            self.image = self.frames[self.aniIndex]
        else:
            self.movementCooldown -= 1
        
        if self.speedup <= 0:
            if self.movementCooldownBase > 5:
                self.movementCooldownBase -= 5
            if self.randomUpperLimit > 100:
                self.randomUpperLimit - 100
            if self.bulletSpeed < 30:    
                self.bulletSpeed += 1
            self.speedup = 400
        else:
            self.speedup -= 1
    
    def bullet_shoot(self):
        return randint(0, self.randomUpperLimit)
  
    def update(self):
        self.movement()