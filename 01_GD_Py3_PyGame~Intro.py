__author__ = 'Nate'

'''
    Pygame tutorial video 1
    Title: Intro
    URL: https://www.youtube.com/watch?v=ujOTNg17LjI&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=1
'''

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()