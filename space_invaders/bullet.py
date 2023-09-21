import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, parentPos, speed, friendly):
        super().__init__()
        if friendly:
            self.image = pygame.image.load("space_invaders/assets/bullet/bullet.png")
            self.rect = self.image.get_rect(midbottom = parentPos)
            self.speed = speed      
        else:
            self.image = pygame.image.load("space_invaders/assets/bullet/enemyBullet.png") 
            self.speed = speed * -1
            self.rect = self.image.get_rect(midtop = parentPos)
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom >= 800:
            self.kill()