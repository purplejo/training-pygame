# coding: utf-8

import sys
import pygame

from data.menus import MainMenu

pygame.init()

main_menu = MainMenu()
main_menu.loop()

pygame.quit()
sys.exit()
