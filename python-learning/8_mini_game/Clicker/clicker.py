import pygame
import random
import json

from debugpy.common.timestamp import current

pygame.init()
screen = pygame.display.set_mode((800, 600)) # Вікно 800x600
clock = pygame.time.Clock() # Для контролю FPS
font = pygame.font.Font(None, 36) # Шрифт для тексту

rand_color = ["blue", "red", "green", "yellow",
              "pink", "purple", "brown", "black"]

class Button:
    def __init__(self, x, y, width, height, color, hover_color="gray"):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color # Колір при наведенні
        self.is_hovered = False # Чи курсор над кнопкою?

    def draw(self, screen):
        # Вибір кольору: якщо наведено — hover_color, інакше — звичайний
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, current_color, self.rect, border_radius=10)

    def update(self, mouse_pos):
        # Перевіряємо, чи курсор над кнопкою
        self.is_hovered = self.rect.collidepoint(mouse_pos)


colors = random.choice(rand_color)

# Створюємо кнопку та лічильник
button = Button(350, 250, 100, 50, colors)
count = 0

try:
    sound = pygame.mixer.Sound('../../5_file-assets/0_assets/for_Clicker/sount/click_sound.wav')  # Завантажуємо звук
except:
    print("Не знайшов файл звуку!")
print("Sound played!")


# start
running = True
while running:
    mous_pos = pygame.mouse.get_pos() # Отримуємо позицію мишки

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(event.pos): # Перевіряємо клік
                count += 1
                button.color = random.choice(rand_color)  # Змінюємо колір кнопки
                sound.play() # Відтворюємо

        button.update(mous_pos) # Оновлюємо стан кнопки (hover)
        screen.fill('white') # Темний фон
        button.draw(screen)

        # Відображаємо лічильник
        text = font.render(f"Clicks: {count}", True, "black")
        screen.blit(text, (50, 50))


        pygame.display.flip() # Оновлення екран
        clock.tick(60) # 60 FPS
