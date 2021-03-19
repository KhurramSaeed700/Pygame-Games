import math
import random
import pygame
from pygame import mixer

# initialize pygame
pygame.init()

# create the screen            (width, height)
screen = pygame.display.set_mode((800, 600))

# Background
bg = pygame.image.load('assets/bg.png')

# Music & SFX
mixer.music.load('C://Users//Dell//PycharmProjects//Pygame Games//001 space ranger game//sfx//bgMusic.mp3')
mixer.music.set_volume(1)
mixer.music.play(-1)

# title and icon of window
pygame.display.set_caption('Space Ranger')
icon = pygame.image.load('assets/spaceship logo.png')  # 16px
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('assets/spaceship.png')  # 64px
playerX = 370
playerY = 480
playerXChange = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXChange = []
enemyYChange = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyXChange.append(0.1)
    enemyYChange.append(40)

# Bullet
# ready = can't see bullet on screen
# fire = bullet moving
bulletImg = pygame.image.load('assets/bomb.png')
bulletX = 0
bulletY = 480
bulletXChange = 0
bulletYChange = 0.7  # bullet speed control
bulletState = 'ready'

# Score
score_value = 0
# font = pygame.font.Font('PressStart2P-vaV7.ttf', 32)
font = pygame.font.Font('D://raima//Videos//Fonts//early_gameboy//Early GameBoy.ttf', 24)
textX = 10
textY = 10

# GameOver Text
gameOverFont = pygame.font.Font('D://raima//Videos//Fonts//early_gameboy//Early GameBoy.ttf', 50)


def show_score(x, y):
    score = font.render('Score ' + str(score_value), True, (133, 150, 198))
    screen.blit(score, (x, y))


def gameOverText():
    gameOver = gameOverFont.render('GAME OVER', True, (133, 150, 198))
    screen.blit(gameOver, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fireBullet(x, y):
    global bulletState
    bulletState = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def ifCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# loop to stop the game window from closing

# clock = pygame.time.Clock()

running = True
while running:
    # clock.tick(60)  # control fps at 60

    # RGB values color of BG
    # screen.fill((11, 24, 87))

    # set space background
    screen.blit(bg, (0, 0))

    # spaceship slowly moves up
    # playerY -= 0.05

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # spaceship moves left to right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange = -0.4  # player movement speed
            if event.key == pygame.K_RIGHT:
                playerXChange = 0.4
            if event.key == pygame.K_SPACE:
                if bulletState == 'ready':
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)
                    bulletSound = mixer.Sound('C://Users//Dell//PycharmProjects//Pygame Games//001 space ranger game//sfx//bullet-fire.mp3')
                    bulletSound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0
    playerX += playerXChange

    # created a boundary so it cannot go outside the window
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            gameOverText()
            break

        enemyX[i] += enemyXChange[i]
        if enemyX[i] <= 0:
            enemyXChange[i] = 0.4
            enemyY[i] += enemyYChange[i]
        elif enemyX[i] >= 736:
            enemyXChange[i] = -0.4
            enemyY[i] += enemyYChange[i]

        # collision
        collision = ifCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound('C://Users//Dell//PycharmProjects//Pygame Games//001 space ranger game//sfx//bullet-hit.mp3')
            explosionSound.play()
            bulletY = 480
            bulletState = 'ready'
            score_value += 1
            # print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # reset bullet
    if bulletY <= 0:
        bulletY = 400
        bulletState = 'ready'

    # Bullet movement
    if bulletState == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletYChange

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
