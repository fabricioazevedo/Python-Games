'''
Created on 18 de jul de 2015

@author: Fabricio
'''

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 5 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
starImg = pygame.image.load('star.png')
starx = 10
stary = 300

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    t = starx^2 
    if t < 400: 
        stary = t
        starx += starx
    if starx > 300:
        starx = 10

    DISPLAYSURF.blit(starImg, (starx, stary))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)