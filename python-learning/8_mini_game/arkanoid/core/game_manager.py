import sys
import pygame
#from .paddle import Paddle
#from .ball import Ball

clock = pygame.time.Clock()
FPS = 60

class GameState:
    def __init__(self, screen, BG_COLOR):
        self.state = "menu"
        self.screen = screen
        #self.paddle = Paddle()
        #self.ball = Ball()
        self.BG_COLOR = BG_COLOR
        self.states = {
            "menu": self.run_menu,
            "playing": self.run_game,
            "game_over": self.run_game_over,
            "shop": self.run_shop
        }

    def change_state(self, new_state):
        if new_state in self.states:
            self.state = new_state
            print(f"Перехід у стан: {self.state}")  # Для дебагу

    def run_menu(self):
        self.screen.fill(self.BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.change_state("playing")
                elif event.key == pygame.K_RETURN:
                    self.change_state("playing")

        pygame.display.flip()  # Оновлюємо екран
        clock.tick(FPS)  # обмеження до 60 FPS

    def run_game(self,):
        self.screen.fill(self.BG_COLOR)

    def run_game_over(self):
        print("Game_over")

    def run_shop(self):
        print("Shop")