import pygame
import random
import json

# Ініціалізація
pygame.init()
pygame.mixer.init()  # Для звуків

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clicker")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
counter = 0

WHITE = (249, 246, 238)
colors = [(204, 0, 204), (255, 0, 102), (51, 204, 51), (204, 204, 0), (0, 153, 153), (165, 42, 42)] # Тепер це справжні кольори



class Button:

    def __init__(self, x, y, width, height):
        self.coordinates = pygame.Rect((x, y,), (width, height))
        self.color = random.choice(colors)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.coordinates, border_radius=8 )


button = Button(350, 250, 100, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            counter += 1
            print(f"Кліків: {counter}")  # Поки що в консоль

    screen.fill(WHITE) # Очищуємо екран
    button.draw(screen) # Малюємо кнопку
    pygame.display.flip() # Оновлюємо екран
    clock.tick(60) # 60 FPS
