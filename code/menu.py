#!/usr/bin/python
# -*- coding: utf-8 -*-

# Menu principal de opções, em que o usuário decide se vai Jogar, ver a pontuação dos jogos anteriores ou fechar a tela

import sys
import pygame
from pygame.rect import Rect
from pygame.surface import Surface
from code.const import WIN_WIDTH, MENU_OPTION, COLOR_WHITE, \
    COLOR_SILVER, COLOR_TURQUOISE

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("asset/MenuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer.music.load("asset/Menu.mp3")
        pygame.mixer.music.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

            self.window.blit(self.surf, self.rect)
            self.menu_text(50, "Asteroid", COLOR_SILVER, (WIN_WIDTH // 2, 70))
            self.menu_text(50, "Run", COLOR_SILVER, (WIN_WIDTH // 2, 120))

            for i in range(len(MENU_OPTION)):
                color = COLOR_TURQUOISE if i == menu_option else COLOR_WHITE
                self.menu_text(20, MENU_OPTION[i], color, (WIN_WIDTH // 2, 200 + 25 * i))

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)