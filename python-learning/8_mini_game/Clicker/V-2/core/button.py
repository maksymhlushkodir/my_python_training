import pygame

class Button:

    def __init__(self, x, y, height, width, text, color):

        self.rect = pygame.Rect(((x, y), (width, height)))
        self.text = text
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=13)

    def is_cliked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)