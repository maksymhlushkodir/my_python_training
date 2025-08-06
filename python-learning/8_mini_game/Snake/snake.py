import pygame
import json
import random
import sys

pygame.init()
pygame.mixer.init()

font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class GameState:
    def __init__(self):
        self.state = "menu" # Початковий стан

        self.start_button = Button(300, 300, 200, 50, "Start", (0, 153, 51))  # Створюємо кнопку
        self.pause_button = Button(600, 15, 50, 50, "⏸", (102, 102, 153))
        self.snake = Snake()
        self.food = Food()
        self.bill = 0
        self.apple = []

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
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.is_clicked(mouse_pos, (0, 183, 81)):
                    self.change_state("playing")  # Перехід у гру
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.change_state("playing")  # Перехід у гру
                elif event.key == pygame.K_1:
                    self.change_state("playing")
        pygame.display.flip()  # Оновлюємо екран
        clock.tick(60) # обмеження до 60 FPS

    def run_game(self):

        screen.fill((0, 102, 0))
        pygame.display.set_caption("Game")
        game_zone = pygame.Rect(45, 65, 710, 490)
        game_zone_decoration= pygame.Rect(25, 45, 750, 530)
        pygame.draw.rect(screen, (68, 102, 0), game_zone_decoration)
        pygame.draw.rect(screen, (0, 153, 51), game_zone)
        pygame.draw.rect(screen, (0, 163, 61), game_zone.inflate(10, 10), border_radius=5)
        text_bill = font.render(f"bill:{self.bill}", True, (0, 0, 0))
        screen.blit(text_bill, (50, 25))

        for ap in self.apple:
            if self.snake.head.colliderect(ap.rect):
                self.bill += 1
                self.apple.remove(ap)
                self.apple.append(Food())

        self.food.draw(screen)
        self.snake.draw(screen)
        self.pause_button.draw(screen)
        self.snake.move()

        if self.snake.head.x > 750:
            self.change_state("game_over")
        elif self.snake.head.x < 30:
            self.change_state("game_over")
        elif self.snake.head.y > 540:
            self.change_state("game_over")
        elif self.snake.head.y < 50:
            self.change_state("game_over")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.pause_button.is_clicked(mouse_pos, (71, 71, 107)):
                    print("OKAY")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("ok")

        pygame.display.flip()  # Оновлюємо екран
        clock.tick(10) # обмеження до 10 FPS

    def run_pause(self):
        print("run pause")

    def run_game_over(self):
        screen.fill((204, 51, 0))
        pygame.display.flip()
        clock.tick(60) # обмеження до 60 FPS

    def run_shop(self):
        print("run shop")

    def change_state(self, new_state):
        if new_state in self.states:  # Перевірка, чи такий стан існує
            self.state = new_state
            print(f"Перехід у стан: {self.state}")  # Для дебагу

class Snake:
    def __init__(self):
        self.head = pygame.Rect(260, 300, 20, 20)
        self.tail = [pygame.Rect(240, 300, 20, 20)]  # Початковий хвіст
        self.status_game = GameState

    def move(self):
        # Оновлюємо хвіст
        for i in range(len(self.tail)-1, 0, -1):
            self.tail[i].x = self.tail[i - 1].x
            self.tail[i].y = self.tail[i - 1].y
        self.tail[0].x, self.tail[0].y = self.head.x, self.head.y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.head.x -= 20
        elif keys[pygame.K_LEFT]:
            self.head.x -= 20
        elif keys[pygame.K_d]:
            self.head.x += 20
        elif keys[pygame.K_RIGHT]:
            self.head.x += 20
        elif keys[pygame.K_w]:
            self.head.y -= 20
        elif keys[pygame.K_UP]:
            self.head.y -= 20
        elif keys[pygame.K_s]:
            self.head.y += 20
        elif keys[pygame.K_DOWN]:
            self.head.y += 20

    def draw(self, screen):
        pygame.draw.rect(screen, (102, 102, 255), self.head)


class Food:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(30, 750),
                                random.randint(20, 530),
                                20, 20)
        self.color = (255, 0, 0)  # Червоний квадратик

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(((x, y), (width, height)))
        self.text = text
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=13)

    def is_clicked(self, mouse_pos, newcolor):
        self.color = newcolor
        return self.rect.collidepoint(mouse_pos)

def main():
    game_state = GameState()
    while True:
        game_state.states[game_state.state]()
        clock.tick(60)  # Загальний FPS для всіх станів

if __name__ == "__main__":
    main()  # Запускаємо гру без зовнішнього циклу