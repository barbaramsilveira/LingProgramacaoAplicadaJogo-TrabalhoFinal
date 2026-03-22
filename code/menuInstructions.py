#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_SILVER, COLOR_TURQUOISE

# Menu de instruções do jogo:

class MenuInstructions:
    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load("asset/MenuBg.png").convert_alpha()
        self.rect = self.bg.get_rect(left=0, top=0)
        self.font_title = pygame.font.SysFont("Lucida Sans Typewriter", 40)
        self.font_instr = pygame.font.SysFont("Arial", 24)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # ESC sai do jogo
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_RETURN:
                        # ENTER avança para iniciar o jogo
                        return

            # fundo
            self.window.blit(self.bg, self.rect)

            # título
            title = self.font_title.render("Instruções do Jogo:", True, COLOR_SILVER)
            self.window.blit(title, (WIN_WIDTH // 2 - title.get_width() // 2, 40))

            # instruções:
            instr1 = self.font_instr.render("← : mover para esquerda", True, COLOR_TURQUOISE)
            instr2 = self.font_instr.render("→ : mover para direita", True, COLOR_TURQUOISE)
            instr3 = self.font_instr.render("↑ : mover para cima", True, COLOR_TURQUOISE)
            instr4 = self.font_instr.render("↓ : mover para baixo", True, COLOR_TURQUOISE)
            instr5 = self.font_instr.render("ESC : sair do jogo", True, COLOR_TURQUOISE)
            instr6 = self.font_instr.render("ENTER : continuar", True, COLOR_TURQUOISE)

            self.window.blit(instr1, (50, WIN_HEIGHT - 230))
            self.window.blit(instr2, (50, WIN_HEIGHT - 200))
            self.window.blit(instr3, (50, WIN_HEIGHT - 170))
            self.window.blit(instr4, (50, WIN_HEIGHT - 140))
            self.window.blit(instr5, (50, WIN_HEIGHT - 110))
            self.window.blit(instr6, (50, WIN_HEIGHT - 80))

            pygame.display.flip()
            clock.tick(30)