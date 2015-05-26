__author__ = 'Nate'

'''
    Pygame tutorial video 9
    Title: Drawing
    URL: https://www.youtube.com/watch?v=nszkfvOXv4w&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=9
'''

import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800, 600))

gameDisplay.fill(black)

# pixels
pix_array = pygame.PixelArray(gameDisplay)
pix_array[10][20] = green

#lines
pygame.draw.line(gameDisplay, blue, (100, 200), (300, 450), 5)

#rectangles
pygame.draw.rect(gameDisplay, red, (400, 400, 50, 25))

#circles
pygame.draw.circle(gameDisplay, white, (150, 150), 75)

#random polygons
pygame.draw.polygon(gameDisplay, green, ((25, 75), (76, 125), (250, 375), (400, 25), (60, 540)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()