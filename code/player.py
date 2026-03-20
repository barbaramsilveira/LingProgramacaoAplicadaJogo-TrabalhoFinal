import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT

class Player:
    def __init__(self, ship_file="Player1.png"):
        self.surf = pygame.image.load("asset/" + ship_file).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (60, 60))
        self.rect = self.surf.get_rect(center=(WIN_WIDTH//2, WIN_HEIGHT-80))
        self.speed = 2
        self.lives = 10



    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.surf, self.rect)