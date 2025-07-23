import pygame
import random

from OpenGL.GL.shaders import found

# Ініціалізація
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Кольори/звуки
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0,)

try:
    sound = pygame.mixer.Sound('../../5_file-assets/0_assets/for_Snake/sound/level_up.mp3') # Завантажуємо звук
except:
    print("ERROR: Sound file not found!")
print("Sound played!")

# Клас Змійки
class Snake:
    def __init__(self):
        self.body = [(400, 300)] # Початкова позиція (голова)
        self.direction = "RIGHT" # Початковий напрямок

    def move(self):
        x, y = self.body[0] # Беремо координати голови
        if self.direction == "UP":
            y -= 20
        elif self.direction == "DOWN":
            y += 20
        elif self.direction == "LEFT":
            x -= 20
        elif self.direction == "RIGHT":
            x += 20

        self.body.insert(0, (x, y)) # Додаємо нову голову
        self.body.pop() # Видаляємо останній сегмент хвоста

    def grow(self):
        # Додаємо новий сегмент на місці останнього (змійка росте)
        self.body.append(self.body[-1])

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 20, 20))

# Клас Їжі
class Food:
    def __init__(self):
        self.position = (random.randrange(0, 800, 20),
                         random.randrange(0, 600, 20))

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], 20, 20))

def key_bord():
    if event.key == pygame.K_UP and snake.direction != "DOWN":
        snake.direction = "UP"
    elif event.key == pygame.K_w and snake.direction != "DOWN":
        snake.direction = "UP"

    elif event.key == pygame.K_DOWN and snake.direction != "UP":
        snake.direction = "DOWN"
    elif event.key == pygame.K_s and snake.direction != "UP":
        snake.direction = "DOWN"

    elif event.key == pygame.K_RIGHT  and snake.direction != "LEFT":
        snake.direction = "RIGHT"
    elif event.key == pygame.K_d  and snake.direction != "LEFT":
        snake.direction = "RIGHT"

    elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
        snake.direction = "LEFT"
    elif event.key == pygame.K_a and snake.direction != "RIGHT":
        snake.direction = "LEFT"

# Головний цикл
snake = Snake()
food = Food()
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            key_bord()

    snake.move()

    # Перевірка, чи змійка з'їла їжу
    if snake.body[0] == food.position:
        snake.grow()
        food = Food()  # Нова їжа
        sound.play()  # Відтворюємо звук
        score += 10


    # Малюємо все на екрані
    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)

    # Виводимо рахунок
    font = pygame.font.Font(None, 36)
    text = font.render(f"Рахунок: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(10)  # Швидкість гри (менше = повільніше)