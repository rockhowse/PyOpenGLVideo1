__author__ = 'Nate'

'''
    Pygame tutorial video 3
    Title: Moving An Image
    URL: https://www.youtube.com/watch?v=xh4SV3kF-zk&index=3&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
'''

import pygame

pygame.init()

display_height = 800
display_width = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')


def car(x, y):
    gameDisplay.blit(carImg, (x, y))

x = (display_width/2)
y = (display_height/2)

x_change = 0

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                x_change = 0

    x += x_change

    gameDisplay.fill(white)
    car(x, y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()