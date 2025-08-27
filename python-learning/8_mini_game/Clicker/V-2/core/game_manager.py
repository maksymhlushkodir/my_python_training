import pygame
import json
import sys

class GameState:
    def __init__(self):
        self.state = "menu"

        self.states = {
            "menu": self.run_menu,
            "playing": self.run_game,
            "tree": self.run_tree,
            "manual": self.run_man,
            "restart": self.run_restart
        }

    def run_menu(self):
        print("menu")

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