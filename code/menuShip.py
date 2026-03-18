#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_TURQUOISE, COLOR_SILVER


class MenuShip:
    def __init__(self, window):
        self.window = window

        # carrega o fundo
        self.surf = pygame.image.load("asset/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        # fonte e lista de naves
        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 32)
        self.ships = ["Player1.png", "Player2.png", "Player3.png", "Player4.png", "Player5.png"]
        self.selected = 0

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.selected = (self.selected - 1) % len(self.ships)
                    elif event.key == pygame.K_RIGHT:
                        self.selected = (self.selected + 1) % len(self.ships)
                    elif event.key == pygame.K_RETURN:
                        return self.ships[self.selected]

            # desenha o fundo
            self.window.blit(self.surf, self.rect)

            # título
            title = self.font.render("Escolha sua nave", True, (COLOR_SILVER))
            self.window.blit(title, (WIN_WIDTH // 2 - title.get_width() // 2, 50))

            # desenha todas as naves lado a lado
            for i, ship in enumerate(self.ships):
                img = pygame.image.load("asset/" + ship).convert_alpha()
                img = pygame.transform.scale(img, (80, 80))
                x = WIN_WIDTH // 2 - (len(self.ships) * 90) // 2 + i * 90
                y = WIN_HEIGHT // 2
                self.window.blit(img, (x, y))

                # destaca nave selecionada
                if i == self.selected:
                    pygame.draw.rect(self.window, (COLOR_TURQUOISE), (x - 5, y - 5, 90, 90), 3)

            pygame.display.flip()
            clock.tick(30)