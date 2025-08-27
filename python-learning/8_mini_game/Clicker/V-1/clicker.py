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

try:
    sound_click = pygame.mixer.Sound('../../../5_file-assets/0_assets/for_clicker/sound/click.wav')
    music_menu = pygame.mixer.music.load('../../../5_file-assets/0_assets/for_clicker/music/menu_1.wav')
    pygame.mixer.music.play(-1) # -1 = зациклити
    print("Ok")
except:
    print("Error: file mot found")

class Button:

    def __init__(self, x, y, width, height):
        self.coordinates = pygame.Rect((x, y,), (width, height))
        self.color = random.choice(colors)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.coordinates, border_radius=8 )



    def is_clicked(self, mouse_pos):
        self.color = random.choice(colors)
        return  self.coordinates.collidepoint(mouse_pos)



button = Button(350, 250, 100, 50)

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(mouse_pos):
                sound_click.play()
                counter += 1
                print(f"Кліків: {counter}")  # Поки що в консоль

    screen.fill(WHITE) # Очищуємо екран
    button.draw(screen) # Малюємо кнопку
    # Малюємо лічильник
    text = font.render(f"Clicks: {counter}", True, (0, 0, 0))  # Текст чорного кольору
    screen.blit(text, (50, 50))  # Координати (x, y)
    pygame.display.flip() # Оновлюємо екран
    clock.tick(60) # 60 FPS

pygame.quit()
exit()