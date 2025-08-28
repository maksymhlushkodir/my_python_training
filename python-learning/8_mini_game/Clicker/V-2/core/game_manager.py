import pygame
import json
import sys
from .button import (Button, Text)
clock = pygame.time.Clock()

man_experience = """Every 100 clicks give you 1 Experience point. Invest them in developing your skills to become stronger!"""

class GameState:
    def __init__(self, screen, BG_COLOR, FPS):
        self.state = "menu"
        self.screen = screen
        self.BG_COLOR = BG_COLOR
        self.FPS = FPS
        self.button = Button
        self.text = Text

        self.click_counter = 0
        self.counter_Experience = 0

        self.manualButton = self.button(400, 500, 50, 200, "manual",
                                      (255, 0, 0), (255, 255, 255), 32)

        self.mainButton = self.button(400, 300, 65, 200, "",
                                      (204, 51, 153), (204, 51, 153))

        self.text_click_counter = self.text(500, 250, f"clicks: {self.click_counter}", (0,0,0), 50)
        self.text_counter_Experience = self.text(500, 200, f"Experience: {self.counter_Experience}", (0,0,0), 50)

        self.startButton = self.button(400, 400, 50, 200, "start",
                                       (0, 0, 0), (255, 255, 255), 32)
        self.titleMenu = self.text(500, 250, "Clicker", (0, 0, 0), 100)

        self.restartButton = self.button(700, 400, 50, 150, "restart",
                                      (102, 102, 255), (255, 255, 255))

        self.manRestartButton = self.button(700, 460, 20, 150, "",
                                         (51, 102, 255))

        self.backButton = self.button(400, 500, 50, 200, "back",
                                      (0, 0, 0), (255, 255, 255), 32)

        self.man_Experience = self.text(500, 200, f"{man_experience}", (0, 0, 0), 27)

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
                elif self.manualButton.is_clicked(mouse_pos):
                    self.change_state("manual")

        self.manualButton.draw(self.screen)
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
                elif self.manRestartButton.is_clicked(mouse_pos):
                    self.change_state("restart")
                elif self.restartButton.is_clicked(mouse_pos):
                    run_experience = True
                    while run_experience:
                        if self.click_counter >= 100:
                            self.counter_Experience += 1
                            self.click_counter -= 100
                        elif self.click_counter < 100:
                            run_experience = False

        self.restartButton.draw(self.screen)
        self.manRestartButton.draw(self.screen)
        self.mainButton.draw(self.screen)
        self.text_click_counter.draw(self.screen)
        self.text_counter_Experience.draw(self.screen)
        self.text_counter_Experience.update_text(f"Experience: {self.counter_Experience}")
        self.text_click_counter.update_text(f"clicks: {self.click_counter}")
        pygame.display.flip()
        clock.tick(self.FPS)  # обмеження до 60 FPS

    def run_tree(self):
        pygame.display.set_caption("upgrade tree")
        print("tree")

    def run_man(self):
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.set_caption("man")
        self.screen.fill(self.BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.backButton.is_clicked(mouse_pos):
                    self.change_state("menu")

        self.backButton.draw(self.screen)
        clock.tick(self.FPS)
        pygame.display.flip()

    def run_restart(self):
        pygame.display.set_caption("re:zero")
        mouse_pos = pygame.mouse.get_pos()  # ← ПЕРЕНЕСИ СЮДИ!
        self.screen.fill(self.BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.backButton.is_clicked(mouse_pos):
                    self.change_state("playing")

        self.backButton.draw(self.screen)
        self.man_Experience.draw(self.screen)
        clock.tick(self.FPS)
        pygame.display.flip()


    def change_state(self, new_state):
        if new_state in self.states:
            self.state = new_state
            print(f"Перехід у стан: {self.state}")  # Для дебагу