import pygame
from sys import exit
from random import randint
from player import Player
from bullet import Bullet
from enemy import Enemy

# TODO : ADD BUNKERS / SHIELDS
# TODO : ADD START MENU / GAME OVER MENU / VICTORY MENU
# TODO : ADD SOUND EFFECTS
# TODO : ADD OTHER ALIEN TYPES?
# TODO : BETTER / BONUS ANIMATIONS
# TODO : LEVELS?

pygame.init()

# Screen
screen = pygame.display.set_mode((600, 900))
screenRect = screen.get_rect(topleft = (0, 0))
pygame.display.set_caption("Space Invaders")

background = pygame.image.load("retro_games/space_invaders/assets/screen/background.png")
mainFont = pygame.font.Font("retro_games/space_invaders/assets/Pixeltype.ttf", 65)

playerLifeIndicator = pygame.image.load("retro_games/space_invaders/assets/player/player.png")
playerLifeIndicator = pygame.transform.rotozoom(playerLifeIndicator, 0, 0.1)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player((300, 780)))

playerLives = 3
playerLivesDisplay = mainFont.render(str(playerLives), False, 'White')

shootCooldown = 60

bullets = pygame.sprite.Group()
enemyBullets = pygame.sprite.Group()

enemies = pygame.sprite.Group()
for i in range(30, 510, 40):
    enemies.add(Enemy(i, 100))
for i in range(30, 510, 40):
    enemies.add(Enemy(i, 150))
for i in range(30, 510, 40):
    enemies.add(Enemy(i, 200))
for i in range(30, 510, 40):
    enemies.add(Enemy(i, 250))

changeDir = False
changeCooldown = 0

# Timers
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and shootCooldown <= 0:
                bullets.add(Bullet((player.sprite.rect.center), 20, True))
                shootCooldown = 60
    
    shootCooldown -= 1

    # WIN CONDITION
    if not enemies:
        pygame.quit()
        exit()

    pygame.sprite.groupcollide(bullets, enemies, True, True)
    if pygame.sprite.spritecollide(player.sprite, enemyBullets, True):
        playerLives -= 1
    # LOSE CONDITION
    if playerLives <= 0:
        pygame.quit()
        exit()

    for enemy in enemies:
        # LOSE CONDITION
        if enemy.rect.y >= 740:
            pygame.quit()
            exit()
        if enemy.rect.right >= 580 or enemy.rect.left <= 10:
            changeDir = True
        if enemy.bullet_shoot() == 420:
            enemyBullets.add(Bullet((enemy.rect.center), enemy.bulletSpeed, False))
    
    if changeDir and changeCooldown <= 1:
        for enemy in enemies:
            enemy.movementVal *= -1
            enemy.drop = True
        changeCooldown = 100
    else:
        changeCooldown -= 1
    
    changeDir = False

    screen.blit(background, screenRect.topleft)

    playerLivesDisplay = mainFont.render(str(playerLives), False, 'White')
    screen.blit(playerLivesDisplay, (30, 850))

    if playerLives > 2:
        screen.blit(playerLifeIndicator, (120, 850))
    if playerLives > 1:
        screen.blit(playerLifeIndicator, (70, 850))

    player.draw(screen)
    player.update()

    bullets.draw(screen)
    bullets.update()

    enemyBullets.draw(screen)
    enemyBullets.update()

    enemies.draw(screen)
    enemies.update()

    pygame.display.update()
    clock.tick(60)