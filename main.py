#!/bin/python3

import pygame
from pygame.locals import *
from mario import Mario

SIZE = WIDTH, HEIGHT = 640, 360
TITLE = 'Mario animations'
FPS = 60

pygame.init()

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()
done = False
delta = 0

mario = Mario(SIZE, center=(110, 110))

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    is_key_pressed = pygame.key.get_pressed()

    if is_key_pressed[K_ESCAPE]:
        done = True

    left = is_key_pressed[K_a] or is_key_pressed[K_LEFT]
    right = is_key_pressed[K_d] or is_key_pressed[K_RIGHT]
    running = is_key_pressed[K_LSHIFT] or is_key_pressed[K_RSHIFT]

    if is_key_pressed[K_w] or is_key_pressed[K_UP] or is_key_pressed[K_SPACE]:
        mario.jump()

    mario.walk((right - left), running)

    mario.update(delta)
    
    screen.fill((0, 0, 0))
    screen.blit(mario.image, mario.rect)

    pygame.display.flip()
    delta = clock.tick(FPS)

pygame.quit()
