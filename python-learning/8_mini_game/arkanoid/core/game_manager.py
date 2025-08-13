import pygame
#from .paddle import Paddle
#from .ball import Ball
from button import Button

class GameState:
    def __init__(self, screen, BG_COLOR):
        self.screen = screen
        self.start_button = Button(300, 300, 200, 50, "Start", (0, 153, 51))
        self.state = "menu"
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
        print("MENU")
        self.screen.fill(self.BG_COLOR)
        #self.start_button.draw(self.screen)

    def run_game(self,):
        print("Playing")

    def run_game_over(self):
        print("Game_over")

    def run_shop(self):
        print("Shop")