# coding: utf-8

import sys

import pygame
import pygame.locals as pg

from tools import softwares

from models import menus

pygame.init()

clock = pygame.time.Clock()
screen = softwares.Screen(title="Lab")
keyboard = softwares.Keyboard()
mouse = softwares.Mouse()

option_A = menus.Option(message="OPTION A")
option_B = menus.Option(message="OPTION B", previous_option=option_A, next_option=option_A)

main_menu = menus.Menu(options=[option_A, option_B])

while screen.running:
    events = pygame.event.get()
    screen.update(events)
    keyboard.update(events)
    mouse.update(events)

    if keyboard.push(pg.K_ESCAPE):
        screen.running = False

    main_menu.loop()

    pygame.display.update()
    clock.tick(120)

pygame.quit()
sys.exit()
