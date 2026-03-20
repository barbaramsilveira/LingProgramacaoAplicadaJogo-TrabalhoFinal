import pygame
from pygame.constants import KEYDOWN, K_RETURN, K_BACKSPACE
from pygame.font import Font
from datetime import datetime

from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_SILVER, COLOR_TURQUOISE
from code.DBProxy import DBProxy


class ScoreMenu:
    def __init__(self, window: Surface):
        self.window = window
        # fundo
        self.surf = pygame.image.load("asset/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 22)

    def run(self):
        db_proxy = DBProxy("DBScore")
        scores = db_proxy.retrieve_top5()
        db_proxy.close()

        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == KEYDOWN:
                    return

            self.window.blit(self.surf, self.rect)
            title = self.font.render("Ranking de Pontuação", True, COLOR_SILVER)
            self.window.blit(title, (WIN_WIDTH // 2 - title.get_width() // 2, 50))

            # cada linha: id, name, ship, score, date
            for i, s in enumerate(scores):
                _, name, ship, score, date = s
                text = self.font.render(
                    f"{i+1}. {name} - {score} - {date}",
                    True,
                    COLOR_TURQUOISE,
                )
                self.window.blit(text, (40, 120 + i * 30))

            pygame.display.flip()
            clock.tick(30)


class Score:
    def __init__(self, window: Surface, ship_file: str):
        self.window = window
        self.ship_file = ship_file
        self.surf = pygame.image.load("asset/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, score: int, player_name: str = None):
        db_proxy = DBProxy("DBScore")

        # se já veio o nome do Level, usa direto
        if player_name:
            db_proxy.save({
                "name": player_name,
                "ship": self.ship_file,
                "score": score,
                "date": get_formatted_date()
            })
            db_proxy.close()
            ScoreMenu(self.window).run()
            return

        # caso contrário, pede input do jogador
        name = ""
        while True:
            self.window.blit(self.surf, self.rect)
            self._draw_text(48, "GAME OVER", COLOR_SILVER, (WIN_WIDTH // 2, 100))
            self._draw_text(24, "Digite seu nome (até 4 letras):", COLOR_TURQUOISE, (WIN_WIDTH // 2, 200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) > 0:
                        db_proxy.save({
                            "name": name,
                            "ship": self.ship_file,
                            "score": score,
                            "date": get_formatted_date()
                        })
                        db_proxy.close()
                        ScoreMenu(self.window).run()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self._draw_text(32, name, COLOR_TURQUOISE, (WIN_WIDTH // 2, 250))
            pygame.display.flip()

    def _draw_text(self, size: int, text: str, color: tuple, center: tuple):
        font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        surf: Surface = font.render(text, True, color).convert_alpha()
        rect: Rect = surf.get_rect(center=center)
        self.window.blit(surf, rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"