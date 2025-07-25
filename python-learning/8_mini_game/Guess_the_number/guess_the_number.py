import pygame
import random
import json

pygame.init()
pygame.mixer.init()

WHITE = (249, 246, 238)
BLACK = (0, 0, 0)
color_start_button = (0, 204, 102)
color_counter_button = (153, 153, 255)
color_re_zero_button = (0, 102, 153)
color_hint_button = (204, 0, 0)
color_input_button = (153, 0, 153)
color_record_button = (255, 153, 0)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guess the number")
clock = pygame.time.Clock()
counter = 0
mouse_pos = pygame.mouse.get_pos()

try:
    sound_click = pygame.mixer.Sound('../../5_file-assets/0_assets/for_guess_the_number/sound/click.wav')
    music_menu = pygame.mixer.music.load('../../5_file-assets/0_assets/for_guess_the_number/music/music_8-bit_level_4.wav')
    pygame.mixer.music.play(-1)  # -1 = зациклити
    print("Ok")
except:
    print("Error: file mot found")


base_font = pygame.font.Font(None, 28)
pc_number = random.randint(1, 100)
print(pc_number)
User_text = ''

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.coordinates = pygame.Rect((x, y), (width, height))
        self.text = text
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.coordinates, border_radius=12)
        text_surface = base_font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.coordinates.center)
        surface.blit(text_surface, text_rect)

    def update_text(self, new_text):
        self.text = new_text  # Змінюємо текст

    def is_clicked(self, mouse_pos):
        return self.coordinates.collidepoint(mouse_pos)


start_button = Button(300, 400, 200, 60, "Try", color_start_button)
counter_button = Button(90, 400, 125, 60, f"counter:", color_counter_button)
re_zero_button = Button(590, 400, 125, 60, "RE:ZERO", color_re_zero_button)
hint_button = Button(300, 100, 200, 100, '', color_hint_button)
input_button = Button(350, 270, 100, 60, 'input:', color_input_button)
record_button = Button(340, 65, 125, 40, f'record:', color_record_button)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_clicked(mouse_pos):
                sound_click.play()
            elif counter_button.is_clicked(mouse_pos):
                sound_click.play()
            elif re_zero_button.is_clicked(mouse_pos):
                sound_click.play()
            #...

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Натиснута "1"
                User_text += "1"  # Додаємо цифру до рядка
            elif event.key == pygame.K_2:
                print(2)
            elif event.key == pygame.K_3:
                print(3)
            elif event.key == pygame.K_4:
                print(4)
            elif event.key == pygame.K_5:
                print(5)
            elif event.key == pygame.K_6:
                print(6)
            elif event.key == pygame.K_7:
                print(7)
            elif event.key == pygame.K_8:
                print(8)
            elif event.key == pygame.K_9:
                print(9)
            elif event.key == pygame.K_0:
                print(0)
            elif event.key == pygame.K_BACKSPACE:
                User_text = User_text[:-1]  # Видаляємо останній символ

                hint_text = ""
                if User_text < pc_number:
                    hint_text = "more! ▲"
                elif User_text > pc_number:
                    hint_text = "Less! ▼"
                elif User_text == pc_number:
                    hint_text = "Correct!"

            elif event.key == pygame.K_ESCAPE:  # ESC
                print("Are you pressing ESC? Does Echidna (re:zero) offer tea?")
                running = False

    screen.fill(WHITE)
    counter_button.draw(screen)
    record_button.draw(screen)
    start_button.draw(screen)
    re_zero_button.draw(screen)
    hint_button.draw(screen)
    input_button.draw(screen)


    pygame.display.flip()  # Оновлюємо екран
    clock.tick(60)  # 60 FPS

pygame.quit()
exit()
