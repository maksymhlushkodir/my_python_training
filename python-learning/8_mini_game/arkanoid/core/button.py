import pygame

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect((x,y),(width,height))
        self.text = text
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, self.text, border_radius=13)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)