import pygame
from sys import exit
from paddle import Paddle
from ball import Ball

pygame.init()

# Screen
screen = pygame.display.set_mode((1000, 600))
screenRect = screen.get_rect(topleft = (0, 0))
pygame.display.set_caption("Pong")

background = pygame.image.load("pong/assets/background.png")
midline = pygame.image.load("pong/assets/middle.png")

# Score
mainFont = pygame.font.Font("pong/assets/Pixeltype.ttf", 100)

player1ScoreValue = 0
player2ScoreValue = 0

cooldown = 0

player1Score = mainFont.render(str(player1ScoreValue), False, 'White')
player2Score = mainFont.render(str(player2ScoreValue), False, 'White')

# Groups
players = pygame.sprite.Group()
players.add(Paddle(screenRect.midleft, True))
players.add(Paddle(screenRect.midright, False))

ball = pygame.sprite.GroupSingle()
ball.add(Ball())

# Timers
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if pygame.sprite.spritecollide(ball.sprite, players, False):
        ball.sprite.xMovement *= -1
    
    if ball.sprite.rect.x >= 1000 and cooldown <= 0:
        player1ScoreValue += 1
        cooldown = 50

    elif ball.sprite.rect.x <= 0 and cooldown <= 0:
        player2ScoreValue += 1
        cooldown = 50
    
    cooldown -= 1
    
    screen.blit(background, (0, 0))
    screen.blit(midline, (485, 0))

    player1Score = mainFont.render(str(player1ScoreValue), False, 'White')
    player2Score = mainFont.render(str(player2ScoreValue), False, 'White')

    screen.blit(player1Score, (100, 50))
    screen.blit(player2Score, (900, 50))

    players.draw(screen)
    players.update()

    ball.draw(screen)
    ball.update()

    pygame.display.update()
    clock.tick(60)