import json
import random
import pygame
from numpy.ma.core import correlate

# Базова ініціалізація
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Розмір вікна
pygame.display.set_caption("Memory Game") # Титул
clock = pygame.time.Clock() # Для контролю FPS

class Button: # Клас для кнопки
    def __init__(self, x, y, width, height, text, color, hover_color=None, sound_path=None):
        self.rect = pygame.Rect(x, y, width, height)  # Область кнопки для кліків
        self.text = text
        self.color = color # Основний колір
        self.hover_color = hover_color if hover_color else color # Колір при наведенні
        self.is_hovered = False  # Чи курсор над кнопкою


    def draw(self, screen):
        # Малюємо кнопку (колір залежить від наведення)
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, current_color, self.rect, border_radius=12) # Закруглені кути

        # Текст на кнопці (якщо потрібно)
        if self.text:
            font = pygame.font.Font(None, 36) # Шрифт
            text_surface = font.render(self.text, True, "black")  # Чорний текст
            text_rect = text_surface.get_rect(center=self.rect.center)  # Центруємо
            screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)  # Перевіряємо наведення

# Створення кнопок (колір, позиція, розмір)
buttons = [
    Button(100, 100, 120, 120, "", "red"),     # Червона
    Button(300, 100, 120, 120, "", "blue"),    # Синя
    Button(100, 300, 120, 120, "", "green"),   # Зелена
    Button(300, 300, 120, 120, "", "yellow")   # Жовта
]

# Початок гри (якщо можна так сказати)
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()  # Отримуємо позицію мишки

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#FFFAFA")  # Твій колір! Pygame підтримує HEX у вигляді рядка :)

    # Малюємо кнопки та перевіряємо наведення
    for button in buttons:
        button.check_hover(mouse_pos)
        button.draw(screen)

    pygame.display.flip()
    clock.tick(60)
