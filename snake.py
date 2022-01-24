import pygame
import random
from pygame.locals import *

pygame.init()

windw_width, windw_height = 600, 500
windw = pygame.display.set_mode((windw_width, windw_height))
background = pygame.image.load('/Users/ekaterinak/Downloads/696.jpg')
pygame.display.set_caption("Прожорливая змейка")

# arguments:
x_snake = 0
y_snake = 0
delta_x, delta_y = 1, 0
block = 10
length = 1
speed = 5
snake_color = (0, 255, 90)
snake_length = []


class Food:
    x = 0
    y = 0

    def new_place(self):
        self.x = round(random.randrange(0, windw_height) / 10.0) * 10.0
        self.y = round(random.randrange(0, windw_width) / 10.0) * 10.0


apple = Food()
apple.new_place()


def snake(block, snake_length):
    for x in snake_length:
        pygame.draw.rect(windw, snake_color, [x[0], x[1], block, block])


# actions:
game_over = False
while not game_over:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    move = pygame.key.get_pressed()
    if move[pygame.K_LEFT]:
        delta_x = -1
        delta_y = 0
    elif move[pygame.K_RIGHT]:
        delta_x = 1
        delta_y = 0
    elif move[pygame.K_UP]:
        delta_x = 0
        delta_y = -1
    elif move[pygame.K_DOWN]:
        delta_x = 0
        delta_y = 1

    x_snake += delta_x * speed
    y_snake += delta_y * speed

    if x_snake > windw_width:
        x_snake = 0
    elif x_snake < 0:
        x_snake = windw_width
    elif y_snake > windw_height:
        y_snake = 0
    elif y_snake < 0:
        y_snake = windw_height

    windw.fill((0, 0, 0))
    windw.blit(background, (0, 0))
    pygame.draw.rect(windw, snake_color, [x_snake, y_snake, block, block])
    pygame.draw.rect(windw, (255, 0, 0), (apple.x, apple.y, block, block))

    snake_Head = []
    snake_Head.append(x_snake)
    snake_Head.append(y_snake)
    snake_length.append(snake_Head)

    if len(snake_length) > length:
        del snake_length[0]

    for i in snake_length[:-1]:
        if i == snake_Head:
            game_over = True

    snake(block, snake_length)

    pygame.display.update()

    if x_snake == apple.x and y_snake == apple.y:
        length += 1


pygame.quit()
quit()
