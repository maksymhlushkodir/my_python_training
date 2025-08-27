import pygame
from core.game_manager import GameState
from settings import (SCREEN_HEIGHT, SCREEN_WIDTH, BG_COLOR, FPS)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = GameState(screen, BG_COLOR, FPS)

    running = True
    while running:
        game.states[game.state]()

if __name__ == "__main__":
    main() # Запускаємо гру без зовнішнього циклу