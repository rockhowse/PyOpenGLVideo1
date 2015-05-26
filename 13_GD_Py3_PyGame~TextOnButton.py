__author__ = 'Nate'

'''
    Pygame tutorial video 13
    Title: TextOnButtons
    URL: https://www.youtube.com/watch?v=OsbyjYuvQk4&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=13
'''

import pygame
import time
import random

pygame.init()

display_height = 800
display_width = 600

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

car_width = 57
car_height = 94

block_color = (53, 115, 255)

gameDisplay = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

largeText = pygame.font.Font("freesansbold.ttf", 115)
smallText = pygame.font.Font("freesansbold.ttf", 20)

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))
    pygame.display.flip()

def things(thing_x, thing_y, thing_width, thing_height, color):
    pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_width, thing_height])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width/2, display_height/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.flip()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed')

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = (display_width/2, display_height/2)
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        green_btn_color = green
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            green_btn_color = bright_green
        pygame.draw.rect(gameDisplay, green_btn_color, (150, 450, 100, 50))

        TextSurf, TextRect = text_objects("GO!", smallText)
        TextRect.center = (150+(100/2), 450+(50/2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        pygame.display.flip()

def game_loop():

    x = (display_width/2)
    y = (display_height/2)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    dodged = 0

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

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
           crash()

        if thing_starty > display_height+thing_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += dodged * 1.2

        if y < thing_starty+thing_height and thing_starty < y+car_height:
            if ((x > thing_startx) and (x < thing_startx + thing_width)) or\
               ((x+car_width > thing_startx) and (x+car_width < thing_startx + thing_width)):
                crash()

        pygame.display.flip()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()