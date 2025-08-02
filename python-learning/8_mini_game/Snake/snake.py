import pygame
import json
import random

pygame.init()
pygame.mixer.init()

font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class GameState:
    def __init__(self):
        self.state = "menu" # Початковий стан
        self.start_button = Button(300, 300, 200, 50, "Start", (0, 153, 51))  # Створюємо кнопку
        self.states = {
            "menu": self.run_menu,
            "playing": self.run_game,
            "pause": self.run_pause,
            "game_over": self.run_game_over,
            "shop": self.run_shop
        }

    def run_menu(self):

        screen.fill((102, 102, 51))
        pygame.display.set_caption("Menu")
        text_title = font.render("Snake", True, (0, 0, 0))
        screen.blit(text_title, (365, 200))
        self.start_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("ok")
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_1):
                self.change_state("playing")  # Перехід у гру
        pygame.display.flip()  # Оновлюємо екран
        clock.tick(10)

    def run_game(self):
        print("run game")

        screen.fill((0, 153, 51))
        pygame.display.set_caption("Game")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("ok")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print("ok")
        pygame.display.flip()  # Оновлюємо екран
        clock.tick(10)

    def run_pause(self):
        print("run pause")

    def run_game_over(self):
        print("run game over")

    def run_shop(self):
        print("run shop")

    def change_state(self, new_state):
        if new_state in self.states:  # Перевірка, чи такий стан існує
            self.state = new_state
            print(f"Перехід у стан: {self.state}")  # Для дебагу

class Snake:
    def __init__(self):
        self.head = pygame.Rect(400, 300, 20, 20)
        self.tail = [pygame.Rect(380, 300, 20, 20)]  # Початковий хвіст
        self.direction = "RIGHT"

    def move(self):
        # Оновлюємо хвіст
        for i in range(len(self.tail)-1, 0, -1):
            self.tail[i].x = self.tail[i - 1].x
            self.tail[i].y = self.tail[i - 1].y
        self.tail[0].x, self.tail[0].y = self.head.x, self.head.y

        # Рухаємо голову
        if self.direction == "RIGHT":
            self.head.x += 20
        elif self.direction == "LEFT":
            self.head.x -= 20
        elif self.direction == "UP":
            self.head.y += 20
        elif self.direction == "DOWN":
            self.head.y -= 20

    def update(self):
        print("Hello<-_->")

class Food:
    def __init__(self):
        self.rect = (random.randint(0, 799),
                     random.randint(0, 599),
                     20, 20)

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = ((x, y), (width, height))
        self.text = text
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=13)

def main():
    print("OK bro")
    game_state = GameState()

    while True:
        # Викликаємо функцію-обробник поточного стану
        game_state.states[game_state.state]()

        # Обробка подій (наприклад, закриття вікна)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

running = True
while running:
    main()