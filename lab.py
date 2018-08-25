# coding: utf-8

import sys

import pygame
import pygame.locals as pg

from tools import softwares

pygame.init()

clock = pygame.time.Clock()
screen = softwares.Screen(title="Lab")
keyboard = softwares.Keyboard()

while screen.running:
    events = pygame.event.get()
    screen.update(events)
    keyboard.update(events)

    if keyboard.push(pg.K_ESCAPE):
        screen.running = False
    if keyboard.push('+', 99):
        print("+")

    pygame.display.update()
    clock.tick(120)

pygame.quit()
sys.exit()
