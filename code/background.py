#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT

# Define o fundo principal do jogo

class Background:
    def __init__(self, filename="background.png", speed=2):
        self.surf = pygame.image.load("asset/background.png").convert()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.speed = speed
        self.y1 = 0
        self.y2 = -self.surf.get_height()

    def move(self):
        # move para baixo
        self.y1 += self.speed
        self.y2 += self.speed

        # reposiciona quando sai da tela
        if self.y1 >= self.surf.get_height():
            self.y1 = self.y2 - self.surf.get_height()
        if self.y2 >= self.surf.get_height():
            self.y2 = self.y1 - self.surf.get_height()

    def draw(self, window):
        window.blit(self.surf, (0, self.y1))
        window.blit(self.surf, (0, self.y2))