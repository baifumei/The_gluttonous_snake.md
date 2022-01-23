import pygame
import random
from pygame.locals import *

pygame.init()

windw_width, windw_height = 600, 500
windw = pygame.display.set_mode((windw_width, windw_height))
pygame.display.set_caption("Прожорливая змейка")

# параметры
x = 0
y = 0
delta_x, delta_y = 1, 0
width = 10
height = 10
lenght = 1
x_food = 50
y_food = 50
speed = 5
snake_color = (0, 255, 90)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

# creat a snake)))
    pygame.draw.rect(windw, snake_color, (x, y, height, width))
    pygame.display.update()

pygame.quit()
quit()
