#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

# Fluxo principal do jogo

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu
from code.menuName import MenuName
from code.menuShip import MenuShip
from code.menuIntro import MenuIntro          # nova tela de introdução
from code.menuInstructions import MenuInstructions
from code.score import ScoreMenu

class Game:
    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:  # Start
                ship_menu = MenuShip(self.window)
                chosen_ship = ship_menu.run()

                name_menu = MenuName(self.window)
                player_name = name_menu.run()

                intro = MenuIntro(self.window)
                intro.run()

                menu_instr = MenuInstructions(self.window)
                menu_instr.run()

                level = Level(self.window, 'Level 1', chosen_ship, player_name)
                score = level.run()

            elif menu_return == MENU_OPTION[1]:  # Score
                score_menu = ScoreMenu(self.window)
                score_menu.run()

            elif menu_return == MENU_OPTION[2]:  # Exit
                pygame.quit()
                sys.exit()