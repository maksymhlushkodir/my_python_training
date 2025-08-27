import pygame
import json
import sys
from .button import Button
clock = pygame.time.Clock()

class GameState:
    def __init__(self, screen, BG_COLOR, FPS):
        self.state = "menu"
        self.screen = screen
        self.BG_COLOR = BG_COLOR
        self.FPS = FPS
        self.button = Button

        self.startButton = self.button(300, 400, 50, 200, "start",
                                       (0, 0, 0), (255, 255, 255), 32)

        self.states = {
            "menu": self.run_menu,
            "playing": self.run_game,
            "tree": self.run_tree,
            "manual": self.run_man,
            "restart": self.run_restart
        }

    def run_menu(self):
        mouse_pos = pygame.mouse.get_pos()  # ← ПЕРЕНЕСИ СЮДИ!
        self.screen.fill(self.BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.startButton.is_clicked(mouse_pos):
                    self.change_state("playing")

        self.startButton.draw(self.screen)
        pygame.display.flip()
        clock.tick(self.FPS)  # обмеження до 60 FPS


    def run_game(self):
        print("game")

    def run_tree(self):
        print("tree")

    def run_man(self):
        print("man")

    def run_restart(self):
        print("restart")

    def change_state(self, new_state):
        if new_state in self.states:
            self.state = new_state
            print(f"Перехід у стан: {self.state}")  # Для дебагу