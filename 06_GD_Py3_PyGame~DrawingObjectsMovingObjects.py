__author__ = 'Nate'

'''
    Pygame tutorial video 6
    Title: Drawing Objects Moving Objects
    URL: https://www.youtube.com/watch?v=zMN9kRLD1DA&index=6&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
'''

import pygame
import time
import random

pygame.init()

display_height = 800
display_width = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 57

gameDisplay = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def things(thing_x, thing_y, thing_width, thing_height, color):
    pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_width, thing_height])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width/2, display_height/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.flip()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():

    x = (display_width/2)
    y = (display_height/2)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            elif event.type == pygame.KEYUP:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x, y)

        if x > display_width - car_width or x < 0:
           crash()

        if thing_starty > display_height+thing_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)

        pygame.display.flip()
        clock.tick(60)

game_loop()
pygame.quit()
quit()