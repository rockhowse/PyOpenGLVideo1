__author__ = 'Nate'

'''
    Pygame tutorial video 4
    Title: AddingBoundaries
    URL: https://www.youtube.com/watch?v=NjvIooRpuH4&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=4
'''

import pygame

pygame.init()

display_height = 600
display_width = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 57

gameDisplay = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def game_loop():

    x = (display_width/2)
    y = (display_height/2)

    x_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            elif event.type == pygame.KEYUP:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x, y)

        if x > display_width - car_width or x < 0:
            gameExit = True

        pygame.display.flip()
        clock.tick(60)

game_loop()
pygame.quit()
quit()