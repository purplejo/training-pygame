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

option_A = menus.Option(message="OPTION A", action=lambda: print("It's ALIVE!!!"))
option_B = menus.Option(pos=(0, 100), message="OPTION B", previous_option=option_A, next_option=option_A)

while screen.running:
    events = pygame.event.get()
    screen.update(events)
    keyboard.update(events)
    mouse.update(events)

    if keyboard.push(pg.K_ESCAPE):
        screen.running = False
    if keyboard.push('+', 99):
        print("+")

    if mouse.move():
        for option in [option_A, option_B]:
            if mouse.inside(option.area):
                option.onfocus()
                break
            else:
                option.onblur()

    if mouse.push(1, 99):
        for option in [option_A, option_B]:
            if mouse.inside(option.area):
                option.apply()
                break

    option_A.blit_on(screen)
    option_B.blit_on(screen)

    pygame.display.update()
    clock.tick(120)

pygame.quit()
sys.exit()
