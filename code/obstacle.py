#!/usr/bin/python
# -*- coding: utf-8 -*-

# Obstáculos do jogo

import pygame, random
from code.const import WIN_WIDTH, WIN_HEIGHT

class Obstacle:
    def __init__(self):
        # carrega imagem do asteroide
        self.surf = pygame.image.load("asset/Asteroid.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (40, 40))
        # posição inicial aleatória
        x = random.randint(0, WIN_WIDTH - 40)
        y = random.randint(-150, -40)  # começa fora da tela
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.speed = random.randint(3, 6)

    def move(self):
        self.rect.y += self.speed
        if self.rect.top > WIN_HEIGHT:
            self.rect.x = random.randint(0, WIN_WIDTH - 40)
            self.rect.y = random.randint(-150, -40)
            self.speed = random.randint(3, 6)

    def draw(self, window):
        window.blit(self.surf, self.rect)