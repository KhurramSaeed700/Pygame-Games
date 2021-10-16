import os
import pygame
from pygame import mixer

pygame.font.init()  # initialize pygame font library
pygame.mixer.init()

width, height = 900, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Second Game...')

red_hit = pygame.USEREVENT + 1  # for handling collisions
blue_hit = pygame.USEREVENT + 2

# Colors
white_color = (255, 255, 255)
black_color = (0, 0, 0)
red_color = (255, 0, 0)
blue_color = (0, 100, 255)

fps = 60
shipSize = 60  # size of ship both width and height
bulletSize = 50  # size of bullet
player_vel = 5  # player velocity
bullet_vel = 7  # bullet speed
max_bullets = 3  # maximum bullets per player

red_battleship_img = pygame.image.load(os.path.join('assets', 'ks.png'))
red_battleship = pygame.transform.rotate(pygame.transform.scale(red_battleship_img, (shipSize, shipSize)),
                                         0)  # RED SPACESHIP
blue_battleship_img = pygame.image.load(os.path.join('assets', 'ss.png'))
blue_battleship = pygame.transform.rotate(pygame.transform.scale(blue_battleship_img, (shipSize, shipSize)),
                                          0)  # BLUE SPACESHIP

border = pygame.Rect(width // 2 - 10, 0, 10, height)  # middle boarder separator

red_bullet_image = pygame.image.load(os.path.join('assets', 'rs_R.png'))
red_bullet = pygame.transform.scale(red_bullet_image, (bulletSize, bulletSize))  # red bullet
blue_bullet_image = pygame.image.load(os.path.join('assets', 'rs_L.png'))
blue_bullet = pygame.transform.scale(blue_bullet_image, (bulletSize, bulletSize))  # blue bullet

bg = pygame.image.load(os.path.join('assets', 'bg.png'))  # bg image

# FONTS
# for pc
health_font = pygame.font.Font('D://Khurram//Videos//FONTS//early_gameboy//Early GameBoy.ttf', 20)
winner_font = pygame.font.Font('D://Khurram//Videos//FONTS//early_gameboy//Early GameBoy.ttf', 40)

# for laptop address
# health_font = pygame.font.Font('D://raima//Videos//Fonts//early_gameboy//Early GameBoy.ttf', 20)
# winner_font = pygame.font.Font('D://raima//Videos//Fonts//early_gameboy//Early GameBoy.ttf', 40)

# Sounds
bulletHit_sound = pygame.mixer.Sound(os.path.join('sfx', 'bullet-hit.mp3'))
bulletFire_sound = pygame.mixer.Sound(os.path.join('sfx', 'bullet-fire.mp3'))
# bg_music_slow = pygame.mixer.Sound(os.path.join('sfx', 'bg-music-slow.mp3'))
bg_music_medium = pygame.mixer.Sound(os.path.join('sfx', 'bg-music-medium.mp3'))
bg_music_fast = pygame.mixer.Sound(os.path.join('sfx', 'bg-music-fast.mp3'))
explosion = pygame.mixer.Sound(os.path.join('sfx', 'lose.mp3'))


def draw_window(Red, Blue, red_bullets, blue_bullets, red_health, blue_health):
    # win.fill(white)  # white bg
    win.blit(bg, (0, 0))  # bg image
    # pygame.draw.rect(win, black, border)  # drawing the boarder

    red_health_text = health_font.render('Health: ' + str(red_health), 1, red_color)
    blue_health_text = health_font.render('Health: ' + str(blue_health), 1, blue_color)
    win.blit(red_health_text, (10, 10))  # display red health
    win.blit(blue_health_text, (width - blue_health_text.get_width() - 10, 10))  # display blue health

    win.blit(red_battleship, (Red.x, Red.y))  # draw player red
    win.blit(blue_battleship, (Blue.x, Blue.y))  # draw player blue

    for bullet in red_bullets:
        win.blit(red_bullet, (bullet.x, bullet.y))
    for bullet in blue_bullets:
        win.blit(blue_bullet, (bullet.x, bullet.y))

    pygame.display.update()


def red_move(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.y > 0:  # left
        red.y -= player_vel
    if keys_pressed[pygame.K_d] and red.y < 436:  # right
        red.y += player_vel
    if keys_pressed[pygame.K_w] and red.x < 380:  # up
        red.x += player_vel
    if keys_pressed[pygame.K_s] and red.x > 0:  # down
        red.x -= player_vel


def blue_move(keys_pressed, blue):
    if keys_pressed[pygame.K_LEFT] and blue.y < 436:  # left
        blue.y += player_vel
    if keys_pressed[pygame.K_RIGHT] and blue.y > 4:  # right
        blue.y -= player_vel
    if keys_pressed[pygame.K_UP] and blue.x > 450:  # up
        blue.x -= player_vel
    if keys_pressed[pygame.K_DOWN] and blue.x < 840:  # down
        blue.x += player_vel


def handle_bullets(redbuls, bluebuls, Red, Blue):
    for bullet in redbuls:
        bullet.x += bullet_vel
        if Blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(blue_hit))
            redbuls.remove(bullet)
        elif bullet.x > width:
            redbuls.remove(bullet)

    for bullet in bluebuls:
        bullet.x -= bullet_vel
        if Red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            bluebuls.remove(bullet)
        elif bullet.x < 0:
            bluebuls.remove(bullet)


def draw_winner(text, color):
    draw_text = winner_font.render(text, 1, color)
    win.blit(draw_text, (width / 2 - draw_text.get_width() / 2, height / 2))
    pygame.display.update()
    pygame.time.delay(10000)


def main():
    red = pygame.Rect(100, 300, shipSize, shipSize)
    blue = pygame.Rect(700, 300, shipSize, shipSize)

    clock = pygame.time.Clock()

    winner_color = ()

    red_bullets = []
    blue_bullets = []

    red_health = 10
    blue_health = 10

    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height // 2, 10, 10)
                    red_bullets.append(bullet)
                    bulletFire_sound.play()

                if event.key == pygame.K_SPACE and len(blue_bullets) < max_bullets:
                    bullet = pygame.Rect(blue.x, blue.y + blue.height // 2, 10, 10)
                    blue_bullets.append(bullet)
                    bulletFire_sound.play()

            if event.type == red_hit:
                red_health -= 1
                bulletHit_sound.play()

            if event.type == blue_hit:
                blue_health -= 1
                bulletHit_sound.play()

        winner_text = ''
        if red_health <= 0:
            winner_text = 'Blue has Won'
            winner_color = blue_color
        if blue_health <= 0:
            winner_text = 'Red has Won'
            winner_color = red_color
        if winner_text != '':
            draw_winner(winner_text, winner_color)
            break

        keys_pressed = pygame.key.get_pressed()
        red_move(keys_pressed, red)
        blue_move(keys_pressed, blue)
        handle_bullets(red_bullets, blue_bullets, red, blue)  # function to HANDLE COLLISIONS OF BULLETS AND PLAYERS

        draw_window(red, blue, red_bullets, blue_bullets, red_health, blue_health)  # draws everything on screen
    main()


if __name__ == '__main__':
    main()
