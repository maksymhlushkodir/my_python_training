import pygame
from core.game_manager import GameState
from settings import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = GameState(screen, BG_COLOR)

    game.states[game.state]()
    running = True
    while running:

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main() # Запускаємо гру без зовнішнього циклу