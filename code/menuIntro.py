#!/usr/bin/python
# -*- coding: utf-8 -*-

# Menu que explica o objetivo do jogo

import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_SILVER, COLOR_TURQUOISE

class MenuIntro:
    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load("asset/MenuBg.png").convert_alpha()
        self.rect = self.bg.get_rect(left=0, top=0)
        self.font_title = pygame.font.SysFont("Lucida Sans Typewriter", 28)
        self.font_text = pygame.font.SysFont("Lucida Sans Typewriter", 14)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_RETURN:
                        return  # continua para a próxima tela

            # fundo
            self.window.blit(self.bg, self.rect)

            # título
            title = self.font_title.render("Asteroid Run", True, COLOR_SILVER)
            self.window.blit(title, (WIN_WIDTH // 2 - title.get_width() // 2, 40))

            # texto da missão
            line1 = self.font_text.render("Você foi convocado para uma missão secreta no espaço!", True, COLOR_TURQUOISE)
            line2 = self.font_text.render("Seu objetivo é desviar dos asteroides e acumular 1000 pontos.", True, COLOR_TURQUOISE)
            line3 = self.font_text.render("Antes de iniciar, escolha sua nave e siga as instruções.", True, COLOR_TURQUOISE)

            self.window.blit(line1, (20, WIN_HEIGHT - 200))
            self.window.blit(line2, (20, WIN_HEIGHT - 170))
            self.window.blit(line3, (20, WIN_HEIGHT - 140))

            # instrução para continuar
            cont = self.font_text.render("Pressione ENTER para continuar ou ESC para sair", True, COLOR_SILVER)
            self.window.blit(cont, (WIN_WIDTH // 2 - cont.get_width() // 2, WIN_HEIGHT - 80))

            pygame.display.flip()
            clock.tick(30)