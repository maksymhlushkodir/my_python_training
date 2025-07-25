import pygame
import random
import json

pygame.init()
pygame.mixer.init()

WHITE = (249, 246, 238)
BLACK = (0, 0, 0)
color_start_button = (0, 204, 102)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guess the number")
clock = pygame.time.Clock()
counter = 0

base_font = pygame.font.Font(None, 36)
pc_number = random.randint(1, 100)
print(pc_number)
User_text = 'fsdf'

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.coordinates = pygame.Rect((x, y), (width, height))
        self.text = text
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.coordinates, border_radius=12)

    def is_clicked(self, mouse_pos):
        return self.coordinates.collidepoint(mouse_pos)

start_button = Button(300, 600, 200, 100, "Try", color_start_button)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Натиснута "1"
                    print(1)
                elif event.type == pygame.K_2:
                    print(2)
                elif event.type == pygame.K_3:
                    print(3)
                elif event.type == pygame.K_4:
                    print(4)
                elif event.type == pygame.K_5:
                    print(5)
                elif event.type == pygame.K_6:
                    print(6)
                elif event.type == pygame.K_7:
                    print(7)
                elif event.type == pygame.K_8:
                    print(8)
                elif event.type == pygame.K_9:
                    print(9)
                elif event.type == pygame.K_0:
                    print(0)
                elif event.key == pygame.K_ESCAPE:  # ESC
                    print("Тикаєш ESC? Хіба Ехідна пропонує чай??")
                    running = False

    screen.fill(WHITE)
    start_button.draw(screen)
    pygame.display.flip()  # Оновлюємо екран
    clock.tick(60)  # 60 FPS

pygame.quit()
exit()
