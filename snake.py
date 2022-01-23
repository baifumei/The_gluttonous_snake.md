import pygame
import random
from pygame.locals import *

pygame.init()

windw_width, windw_height = 600, 500
windw = pygame.display.set_mode((windw_width, windw_height))
background = pygame.image.load('/Users/ekaterinak/Downloads/696.jpg')
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


class Food:
    x = 0
    y = 0

    def new_place(self):
        self.x = round(random.randrange(0, windw_height) / 10.0) * 10.0
        self.y = round(random.randrange(0, windw_width) / 10.0) * 10.0


apple = Food()
apple.new_place()


# действия
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

    x += delta_x * speed
    y += delta_y * speed

    if x > windw_width:
        x = 0
    elif x < 0:
        x = windw_width
    elif y > windw_height:
        y = 0
    elif y < 0:
        y = windw_height

    if x == apple.x and y == apple.y:
        print("Yummy!!")

    windw.fill((0, 0, 0))
    windw.blit(background, (0, 0))

    pygame.draw.rect(windw, snake_color, (x, y, height, width))
    pygame.draw.rect(windw, (255, 0, 0), (apple.x, apple.y, height, width))
    pygame.display.update()


pygame.quit()
quit()
