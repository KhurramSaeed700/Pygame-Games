import pygame
from pygame.locals import *

clock = pygame.time.Clock()

# constants
screen_width = 1300
screen_height = 950
fps = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invader')

# load image
bg = pygame.image.load('assets/bg.jpg')


def draw_bg():
    screen.blit(bg, (0, 0))


# create spaceship class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        # set movment speed
        speed=8

        # get key press
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= speed
        if key[pygame.K_RIGHT]:
            self.rect.x += speed


# create sprite groups
spaceship_group = pygame.sprite.Group()

# create player
spaceship = Spaceship(int(screen_width / 2), screen_height - 100)
spaceship_group.add(spaceship)

run = True
while run:
    clock.tick(fps)

    # draw background
    draw_bg()

    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update spaceship
    spaceship.update()



    # draw sprite groups
    spaceship_group.draw(screen)

    pygame.display.update()

pygame.quit()
