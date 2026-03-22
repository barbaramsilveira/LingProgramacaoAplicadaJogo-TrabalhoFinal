#!/usr/bin/python
# -*- coding: utf-8 -*-

# Menu para digitação de nome do jogador:

import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_SILVER, COLOR_PURPLE, COLOR_TURQUOISE

class MenuName:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("asset/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 32)
        self.input_text = ""  # texto digitado pelo jogador

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # retorna o nome digitado
                        return self.input_text
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        # adiciona caractere ao texto
                        self.input_text += event.unicode

            # desenha fundo
            self.window.blit(self.surf, self.rect)

            # título
            title = self.font.render("Digite seu nome:", True, (COLOR_SILVER))
            self.window.blit(title, (WIN_WIDTH//2 - title.get_width()//2, 150))

            # texto digitado
            name_surface = self.font.render(self.input_text, True, (COLOR_TURQUOISE))
            self.window.blit(name_surface, (WIN_WIDTH//2 - name_surface.get_width()//2, 220))

            pygame.display.flip()
            clock.tick(30)