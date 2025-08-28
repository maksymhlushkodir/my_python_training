import pygame
import json
import sys
from .button import (Button, Text)
clock = pygame.time.Clock()

class GameState:
    def __init__(self, screen, BG_COLOR, FPS):
        self.state = "menu"
        self.screen = screen
        self.BG_COLOR = BG_COLOR
        self.FPS = FPS
        self.button = Button
        self.text = Text

        self.click_counter = 0
        self.counter_legendary_click = 0

        self.mainButton = self.button(300, 300, 65, 200, "",
                                      (204, 51, 153), (204, 51, 153))
        self.text_click_counter = self.text(400, 250, f"clicks: {self.click_counter}", (0,0,0), 50)

        self.startButton = self.button(300, 400, 50, 200, "start",
                                       (0, 0, 0), (255, 255, 255), 32)
        self.titleMenu = self.text(400, 250, "Clicker", (0, 0, 0), 100)

        self.restartButton = self.button(600, 400, 50, 150, "restart",
                                      (102, 102, 255), (255, 255, 255))

        self.states = {
            "menu": self.run_menu,
            "playing": self.run_game,
            "tree": self.run_tree,
            "manual": self.run_man,
            "restart": self.run_restart
        }

    def run_menu(self):
        pygame.display.set_caption("Menu")
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
        self.titleMenu.draw(self.screen)
        pygame.display.flip()
        clock.tick(self.FPS)  # обмеження до 60 FPS


    def run_game(self):
        pygame.display.set_caption("Clicker")
        mouse_pos = pygame.mouse.get_pos()  # ← ПЕРЕНЕСИ СЮДИ!
        self.screen.fill(self.BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.mainButton.is_clicked(mouse_pos):
                    self.click_counter += 1
                    print(self.click_counter)


        self.restartButton.draw(self.screen)
        self.mainButton.draw(self.screen)
        self.text_click_counter.draw(self.screen)
        self.text_click_counter.update_text(f"clicks: {self.click_counter}")
        pygame.display.flip()
        clock.tick(self.FPS)  # обмеження до 60 FPS

    def run_tree(self):
        pygame.display.set_caption("upgrade tree")
        print("tree")

    def run_man(self):
        pygame.display.set_caption("man")
        print("man")

    def run_restart(self):
        pygame.display.set_caption("re:zero")
        print("restart")

    def change_state(self, new_state):
        if new_state in self.states:
            self.state = new_state
            print(f"Перехід у стан: {self.state}")  # Для дебагу