import pygame

class Button:

    def __init__(self, x, y, height, width, text, color, text_color=(255, 255, 255), font_size=32):

        self.rect = pygame.Rect(((x, y), (width, height)))
        self.text = text
        self.color = color
        self.text_color = text_color  # Новий параметр для кольору тексту
        self.font = pygame.font.SysFont(None, font_size)  # Створюємо шрифт

    def draw(self, surface):
        # Малюємо кнопку
        pygame.draw.rect(surface, self.color, self.rect, border_radius=13)

        # Створюємо текст
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Малюємо текст поверх кнопки
        surface.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)