import pygame
from screeninfo import get_monitors
from sys import exit
from player import Player
from bullet import Bullet
from enemy import Enemy
from shield import Shield

# May come back to these in the future but if i'm being honest this is a silly little game and these really aren't that necessary. 

# TODO : ADD SOUND EFFECTS
# TODO : ADD OTHER ALIEN TYPES?
# TODO : BETTER / BONUS ANIMATIONS
# TODO : LEVELS?
# TODO : GAMEMODES? CLASSIC VS IDK

pygame.init()

def start(destination):

    global width
    global height
    global generalHeightScalar

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

    player.add(Player((int(width / 2), int(height * 13/15)), generalHeightScalar, generalWidthScalar))

    shields.add(Shield((int(width / 8), int(height * 7/9)), width, height))
    shields.add(Shield((int(width * 3/8), int(height * 7/9)), width, height))
    shields.add(Shield((int(width * 5/8), int(height * 7/9)), width, height))
    shields.add(Shield((int(width * 7/8), int(height * 7/9)), width, height))
    
    for i in range(int(width * 2/15), int(width * 2/15) * 7, int(width * 1/15)):
        for t in range(int(height * 1/18), int(height * 1/18) * 5, int(height * 1/18)):
            enemies.add(Enemy(i, t, height, width, generalWidthScalar, generalHeightScalar))
    
    for i in range(int(width * 2/15), int(width * 2/15) * 7, int(width * 1/15)):
        for t in range(int(height * 1/18) + int(height * 11/45), int(height * 1/18) * 5 + int(height * 2/15), int(height * 1/18)):
            enemies.add(Enemy(i, t, height, width, generalWidthScalar, generalHeightScalar))

    global changeDir
    global changeCooldown
    changeDir = False
    changeCooldown = 0  


# General Scalars

for m in get_monitors():
    height = m.height * 5/6

width = height * 2/3

generalWidthScalar = width / 600
generalHeightScalar = height / 900

# Screen
screen = pygame.display.set_mode((width, height))
screenRect = screen.get_rect(topleft = (0, 0))
pygame.display.set_caption("Space Invaders")

background = pygame.image.load("retro_games/space_invaders/assets/screen/background.png")
background = pygame.transform.scale(background, (width, height))
mainFont = pygame.font.Font("retro_games/space_invaders/assets/Pixeltype.ttf", int(65 * generalHeightScalar))

gameover = pygame.image.load("retro_games/space_invaders/assets/screen/gameover.png")
gameover = pygame.transform.scale(gameover, (width, height))
startscreen = pygame.image.load("retro_games/space_invaders/assets/screen/startscreen.png")
startscreen = pygame.transform.scale(startscreen, (width, height))
victoryscreen = pygame.image.load("retro_games/space_invaders/assets/screen/victoryscreen.png")
victoryscreen = pygame.transform.scale(victoryscreen, (width, height))

playerLifeIndicator = pygame.image.load("retro_games/space_invaders/assets/player/player.png")
playerLifeIndicator = pygame.transform.rotozoom(playerLifeIndicator, 0, 0.1 * generalHeightScalar)

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
                bullets.add(Bullet((player.sprite.rect.center), 20, True, generalHeightScalar))
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
            if enemy.rect.y >= height * 13/18:
                screenmode = 1
            if enemy.rect.right >= width * 29/30 or enemy.rect.left <= width * 1/60:
                changeDir = True
            if enemy.bullet_shoot() == 69:
                enemyBullets.add(Bullet((enemy.rect.center), enemy.bulletSpeed, False, generalHeightScalar))
        
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
        screen.blit(playerLivesDisplay, (width * 1/20, height * 17/18))

        if playerLives > 2:
            screen.blit(playerLifeIndicator, (width * 1/5, height * 17/18))
        if playerLives > 1:
            screen.blit(playerLifeIndicator, (width * 7/60, height * 17/18))

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