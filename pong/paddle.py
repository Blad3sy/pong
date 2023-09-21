import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, pos, player1):
        super().__init__()

        self.image = pygame.image.load("pong/assets/paddle.png")
        self.rect = self.image.get_rect(midleft = pos)
        self.player1 = player1

        if not player1:
            self.rect.x -= 10
    
    def input(self):
        keys = pygame.key.get_pressed()
        if self.player1:
            if keys[pygame.K_w]:
                if self.rect.y > 0:
                    self.rect.y -= 10
        
            elif keys[pygame.K_s]:
                if self.rect.y < 525:
                    self.rect.y += 10
        else:
            if keys[pygame.K_UP]:
                if self.rect.y > 0:
                    self.rect.y -= 10
        
            elif keys[pygame.K_DOWN]:
                if self.rect.y < 525:
                    self.rect.y += 10
    
    def update(self):
        self.input()