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
    def __init__(self, x, y, width, height, text, color, hover_color=None, sound_path=None, draw_highlight=False):
        self.rect = pygame.Rect(x, y, width, height)  # Область кнопки для кліків
        self.text = text
        self.color = color # Основний колір
        self.hover_color = hover_color if hover_color else color # Колір при наведенні
        self.is_hovered = False  # Чи курсор над кнопкою
        self.draw_highlight = draw_highlight
        self.normal_color = color  # Зберігаємо оригінальний колір

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

    def draw_highlight(self):
        # Зберігаємо оригінальний колір і встановлюємо яскравіший
        self.normal_color = self.color
        self.color = (min(self.color[0] + 50, 255), min(self.color[1] + 50, 255), min(self.color[2] + 50, 255))

    def draw_normal(self):
        # Повертаємо оригінальний колір
        self.color = self.normal_color

# Створення кнопок (колір, позиція, розмір)
buttons = [
    Button(100, 100, 120, 120, "", (255, 0, 0)),     # Червона
    Button(300, 100, 120, 120, "", (0, 0, 255)),    # Синя
    Button(100, 300, 120, 120, "", (0, 255, 0)),   # Зелена
    Button(300, 300, 120, 120, "", (255, 255, 0))   # Жовта
]

sequence = []  # Послідовність, яку потрібно повторити
player_sequence = []  # Відповідь гравця
level = 1  # Початковий рівень
current_step = 0  # Поточний крок у послідовності
waiting_for_input = False  # Чи чекаємо на введення гравця

def generate_sequence(length):
    colors = ["red", "blue", "green", "yellow"]
    return [random.choice(colors) for _ in range(length)]

def play_sequence():
    for color in sequence:
        button = next(b for b in buttons if b.color == color)  # Знаходимо кнопку за кольором
        button.draw_highlight()  # Підсвічуємо
        pygame.display.flip()
        pygame.time.delay(500)  # Затримка 0.5 сек
        button.draw_normal()  # Повертаємо звичайний вигляд
        pygame.display.flip()
        pygame.time.delay(300)  # Невелика пауза між кольорами

def level_up():
    global level, sequence, player_sequence
    level += 1
    player_sequence = []
    sequence = generate_sequence(level)  # Генеруємо довшу послідовність
    play_sequence()  # Відтворюємо нову послідовність

def game_over():
    global running, level
    print(f"Game Over! Ваш рівень: {level}")
    save_record(level)  # Зберігаємо рекорд (якщо він побитий)
    running = False  # Закриваємо гру (або можна зробити меню рестарту)

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and waiting_for_input:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(mouse_pos):  # Якщо клікнули на кнопку
                    player_sequence.append(button.color)
                    # Перевіряємо, чи гравець помилився
                    if player_sequence[-1] != sequence[len(player_sequence) - 1]:
                        game_over()
                    # Якщо послідовність завершена
                    elif len(player_sequence) == len(sequence):
                        level_up()

    pygame.display.flip()
    clock.tick(60)