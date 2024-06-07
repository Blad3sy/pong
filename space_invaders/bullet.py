import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, parentPos, speed, friendly, heightScalar):
        super().__init__()
        self.heightScalar = heightScalar
        if friendly:
            self.image = pygame.image.load("retro_games/space_invaders/assets/bullet/bullet.png")
            self.image = pygame.transform.rotozoom(self.image, 0, 1 * heightScalar)
            self.rect = self.image.get_rect(midbottom = parentPos)
            self.speed = speed * heightScalar     
        else:
            self.image = pygame.image.load("retro_games/space_invaders/assets/bullet/enemyBullet.png") 
            self.image = pygame.transform.rotozoom(self.image, 0, 1 * heightScalar)
            self.speed = speed * -1 * heightScalar
            self.rect = self.image.get_rect(midtop = parentPos)
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom >= 800 * self.heightScalar:
            self.kill()