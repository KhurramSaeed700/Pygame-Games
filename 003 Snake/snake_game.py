# print('my Code')
#
# import sys
# import random as rnd
# import pygame
#
# pygame.font.init()
#
#
# class Snake:
#     def __int__(self):
#         self.length = 1
#         self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
#         self.direction = rnd.choice([UP, DOWN, LEFT, RIGHT])
#         self.color = (17, 24, 47)
#         self.score=0
#
#     def get_head_post(self):
#         return self.positions[0]
#
#     def turn(self, point):
#         if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
#             return
#         else:
#             self.direction = point
#
#     def move(self):
#         cur = self.get_head_post()
#         x, y = self.direction
#         new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
#         if len(self.position) > 2 and new in self.position[2:]:
#             self.reset()
#         else:
#             self.position.insert(0, new)
#             if len(self.position) > self.length:
#                 self.position.pop()
#
#     def reset(self):
#         self.length = 1
#         self.position = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
#         self.direction = rnd.choice([UP, DOWN, LEFT, RIGHT])
#         self.score=0
#
#     def draw(self, surface):
#         for p in self.position:
#             r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
#             pygame.draw.rect(surface, self.color, r)
#             pygame.draw.rect(surface, (93, 216, 218), r, 1)
#
#     def handle_keys(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_UP:
#                     self.turn(UP)
#                 elif event.key == pygame.K_DOWN:
#                     self.turn(DOWN)
#                 elif event.key == pygame.K_LEFT:
#                     self.turn(LEFT)
#                 elif event.key == pygame.K_RIGHT:
#                     self.turn(RIGHT)
#
#
# class Food:
#     def __init__(self):
#         self.position = (0, 0)
#         self.color = (233, 163, 49)
#         self.randomize_position()
#
#     def randomize_position(self):
#         self.position = (rnd.randint(0, GRID_WIDTH - 1) * GRID_SIZE, rnd.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
#
#     def draw(self, surface):
#         r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
#         pygame.draw.rect(surface, self.color, r)
#         pygame.draw.rect(surface, (93, 216, 218), r, 1)
#
#
# # function to draw a grid
# def drawGrid(surface):
#     for y in range(0, int(GRID_HEIGHT)):
#         for x in range(0, int(GRID_WIDTH)):
#             if (x + y) % 2 == 0:
#                 r = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
#                 pygame.draw.rect(surface, (93, 216, 228), r)
#             else:
#                 rr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
#                 pygame.draw.rect(surface, (84, 194, 205), rr)
#
#
# # Global Variables (capital letters because they remain constant throughout the game)
#
# SCREEN_WIDTH = 480
# SCREEN_HEIGHT = 480
#
# GRID_SIZE = 20
# GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
# GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE
#
# UP = (0, -1)
# DOWN = (0, 1)
# LEFT = (-1, 0)
# RIGHT = (1, 0)
#
# score_font = pygame.font.Font('D://raima//Videos//Fonts//early_gameboy//Early GameBoy.ttf', 20)
#
#
# # myfont = pygame.font.SysFont('monospace', 16)
#
#
# def main():
#     pygame.init()
#
#     clock = pygame.time.Clock()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
#
#     surface = pygame.Surface(screen.get_size())
#     surface = surface.convert()
#     drawGrid(surface)
#
#     snake = Snake()
#     food = Food()
#
#     # score = 0
#     while True:
#         clock.tick(10)
#         snake.handle_keys()
#         drawGrid(surface)
#         snake.move()
#         if snake.get_head_post() == food.position:
#             snake.length += 1
#             snake.score += 1
#             food.randomize_position()
#         snake.draw(surface)
#         food.draw(surface)
#         screen.blit(surface, (0, 0))
#         text = score_font.render("Score {0}".format(snake.score), 1, (0, 0, 0))
#         screen.blit(text, (5, 10))
#         pygame.display.update()
#
#
# main()


print('Youtube Code')
# Youtube Code=========================================


import pygame
import sys
import random


class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        # Special thanks to YouTubers Mini - Cafetos and Knivens Beast for raising this issue!
        # Code adjustment courtesy of YouTuber Elija de Hoog
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * gridsize)) % screen_width), (cur[1] + (y * gridsize)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


class Food():
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width - 1) * gridsize, random.randint(0, grid_height - 1) * gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (84, 194, 205), rr)


screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace", 16)
    score_font = pygame.font.Font('D://raima//Videos//Fonts//early_gameboy//Early GameBoy.ttf', 20)

    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = score_font.render("Score {0}".format(snake.score), 1, (0, 0, 0))
        screen.blit(text, (5, 2))
        pygame.display.update()


main()
