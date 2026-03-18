#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from code.player import Player
from code.obstacle import Obstacle
from code.entityFactory import EntityFactory
from code.const import WIN_WIDTH, WIN_HEIGHT

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode

        # fundo (lista de backgrounds)
        self.bg_list = EntityFactory.get_entity('Level1Bg')

        # player
        self.player = Player(game_mode)  # game_mode aqui é o nome da nave escolhida

        # obstáculos
        self.obstacles = [Obstacle() for i in range(5)]

        # lista de entidades que têm rect (player + obstáculos)
        self.entity_list = self.obstacles + [self.player]

        self.score = 0
        self.font = pygame.font.SysFont("Arial", 24)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # mover e desenhar fundo separado
            for bg in self.bg_list:
                bg.move()
                bg.draw(self.window)

            # mover e desenhar player + obstáculos
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

            # colisão player x obstáculos
            for obs in self.obstacles:
                if self.player.rect.colliderect(obs.rect):
                    self.player.lives -= 1
                    print(f"Colisão! Vidas restantes: {self.player.lives}")
                    # reposiciona o obstáculo para não ficar colidindo em loop
                    obs.rect.y = -50
                    obs.rect.x = random.randint(0, WIN_WIDTH - 40)

                    if self.player.lives <= 0:
                        print("Game Over!")
                        pygame.quit()
                        quit()

            # pontuação
            score_text = self.font.render(f"Score: {self.score}", True, (255,255,255))
            self.window.blit(score_text, (10,10))
            self.score += 1

            pygame.display.flip()
            clock.tick(60)