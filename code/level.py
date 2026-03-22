#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame
from code.player import Player
from code.obstacle import Obstacle
from code.entityFactory import EntityFactory
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.score import Score

# Classe responsável pelas fases do jogo:

class Level:
    def __init__(self, window, name, ship_file, player_name):
        self.window = window
        self.name = name
        self.ship_file = ship_file
        self.player_name = player_name

        # fundo (lista de backgrounds)
        self.bg_list = EntityFactory.get_entity('Level1Bg')

        # player (usa nave escolhida)
        self.player = Player(ship_file)

        # obstáculos
        self.obstacles = [Obstacle() for i in range(5)]
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

            # mover e desenhar fundo
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
                    # reposiciona o obstáculo para não ficar colidindo em loop
                    obs.rect.y = -50
                    obs.rect.x = random.randint(0, WIN_WIDTH - 40)

                    if self.player.lives <= 0:
                        from code.score import Score
                        score_screen = Score(self.window, self.ship_file)
                        score_screen.save(self.score, self.player_name)
                        return self.score

            # Exibe pontuação na tela
            score_text = self.font.render(f"Pontuação: {self.score}", True, (255,255,255))
            self.window.blit(score_text, (10,10))
            self.score += 1

            # Exibe vidas restantes na tela
            lives_text = self.font.render(f"Vidas restantes: {self.player.lives}", True, (255, 255, 255))
            self.window.blit(lives_text, (10, 40))

            pygame.display.flip()
            clock.tick(60)