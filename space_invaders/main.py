import pygame
from sys import exit
from player import Player
from bullet import Bullet
from enemy import Enemy
from shield import Shield

# TODO : ADD START MENU / GAME OVER MENU / VICTORY MENU
# TODO : ADD SOUND EFFECTS
# TODO : ADD OTHER ALIEN TYPES?
# TODO : BETTER / BONUS ANIMATIONS
# TODO : LEVELS?
# TODO : GAMEMODES? CLASSIC VS IDK

pygame.init()

def start(destination):

    player.empty()
    enemies.empty()
    bullets.empty()
    enemyBullets.empty()
    shields.empty()

    global screenmode
    screenmode = destination

    global playerLives
    global playerLivesDisplay
    playerLives = 3
    playerLivesDisplay = mainFont.render(str(playerLives), False, 'White')

    global shootCooldown
    shootCooldown = 60

    player.add(Player((300, 780)))

    shields.add(Shield((75, 700)))
    shields.add(Shield((225, 700)))
    shields.add(Shield((375, 700)))
    shields.add(Shield((525, 700)))
    
    for i in range(80, 560, 40):
        for t in range(50, 250, 50):
            enemies.add(Enemy(i, t))
    
    for i in range(80, 560, 40):
        for t in range(270, 370, 50):
            enemies.add(Enemy(i, t))

    global changeDir
    global changeCooldown
    changeDir = False
    changeCooldown = 0  

# Screen
screen = pygame.display.set_mode((600, 900))
screenRect = screen.get_rect(topleft = (0, 0))
pygame.display.set_caption("Space Invaders")

background = pygame.image.load("retro_games/space_invaders/assets/screen/background.png")
mainFont = pygame.font.Font("retro_games/space_invaders/assets/Pixeltype.ttf", 65)

gameover = pygame.image.load("retro_games/space_invaders/assets/screen/gameover.png")
startscreen = pygame.image.load("retro_games/space_invaders/assets/screen/startscreen.png")
victoryscreen = pygame.image.load("retro_games/space_invaders/assets/screen/victoryscreen.png")

playerLifeIndicator = pygame.image.load("retro_games/space_invaders/assets/player/player.png")
playerLifeIndicator = pygame.transform.rotozoom(playerLifeIndicator, 0, 0.1)

screenmode = 2

# Groups
player = pygame.sprite.GroupSingle()

playerLives = 3

shootCooldown = 60

bullets = pygame.sprite.Group()
enemyBullets = pygame.sprite.Group()

shields = pygame.sprite.Group()

enemies = pygame.sprite.Group()

changeDir = False
changeCooldown = 0

# Timers
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and screenmode == 0:
            if event.key == pygame.K_SPACE and shootCooldown <= 0:
                bullets.add(Bullet((player.sprite.rect.center), 20, True))
                shootCooldown = 60
        elif event.type == pygame.KEYDOWN and screenmode == 1:
            start(2)
        elif event.type == pygame.KEYDOWN and screenmode == 2:
            start(0)
        elif event.type == pygame.KEYDOWN and screenmode == 3:
            start(2)

    if screenmode == 0:
        
        shootCooldown -= 1

        # WIN CONDITION
        if not enemies:
            screenmode = 3

        pygame.sprite.groupcollide(bullets, enemies, True, True)
        if pygame.sprite.spritecollide(player.sprite, enemyBullets, True):
            playerLives -= 1
        # LOSE CONDITION
        if playerLives <= 0:
            screenmode = 1

        for enemy in enemies:
            # LOSE CONDITION
            if enemy.rect.y >= 650:
                screenmode = 1
            if enemy.rect.right >= 580 or enemy.rect.left <= 10:
                changeDir = True
            if enemy.bullet_shoot() == 69:
                enemyBullets.add(Bullet((enemy.rect.center), enemy.bulletSpeed, False))
        
        collisions = pygame.sprite.groupcollide(shields, enemyBullets, False, True)
        if collisions:
            for collider in collisions:
                for shield in shields:
                    if collider.rect.center == shield.rect.center:
                        shield.nextState()

        
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

        shields.draw(screen)

    elif screenmode == 1:
        screen.fill((0, 0, 0))
        screen.blit(gameover, screenRect.topleft)
    
    elif screenmode == 2:
        screen.fill((0, 0, 0))
        screen.blit(startscreen, screenRect.topleft)
    
    elif screenmode == 3:
        screen.fill((0, 0, 0))
        screen.blit(victoryscreen, screenRect.topleft)
    
    pygame.display.update()
    clock.tick(60)