#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu
from code.menuShip import MenuShip   # <-- novo import

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                # chama menu de seleção de nave
                ship_menu = MenuShip(self.window)
                chosen_ship = ship_menu.run()

                # inicia o level com a nave escolhida
                level = Level(self.window, 'Level 1', chosen_ship)
                level_return = level.run()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass