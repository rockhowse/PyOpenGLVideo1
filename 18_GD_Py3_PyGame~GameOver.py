__author__ = 'Nate'

'''
    Pygame tutorial video 18
    Title: Game over
    URL: https://www.youtube.com/watch?v=yogDvU10Mlo&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=18
'''

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

car_width = 57
car_height = 94

block_color = (53, 115, 255)

gameDisplay = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

largeText = pygame.font.SysFont("comicsansms", 115)
smallText = pygame.font.SysFont("comicsansms", 20)

pause_val = False
crash_val = False

def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
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
    global crash_val
    crash_val = True

    TextSurf, TextRect = text_objects("Crashed", largeText)
    TextRect.center = (display_width/2, display_height/2)
    gameDisplay.blit(TextSurf, TextRect)

    while crash_val:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        #gameDisplay.fill(white)

        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit!", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.flip()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = (x+(w/2), y+(h/2))
    gameDisplay.blit(TextSurf, TextRect)

def quit_game():
    pygame.quit()
    quit()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = (display_width/2, display_height/2)
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit!", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.flip()

def unpause():
    global pause_val
    pause_val = False

def pause():
    TextSurf, TextRect = text_objects("Pause", largeText)
    TextRect.center = (display_width/2, display_height/2)
    gameDisplay.blit(TextSurf, TextRect)

    while pause_val:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        #gameDisplay.fill(white)

        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit!", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.flip()

def game_loop():
    global pause_val
    pause_val = False

    global crash_val
    crash_val = True

    x = ((display_width/2)-(car_width/2))
    y = (display_height*0.8)

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
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_p:
                    pause_val = True
                    pause()

            elif event.type == pygame.KEYUP:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        #print (str(x) + "|" + str(display_width))

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
quit_game()