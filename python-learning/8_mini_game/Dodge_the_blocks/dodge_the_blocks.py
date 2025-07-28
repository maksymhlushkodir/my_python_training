import random
import pygame
import json

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dodge the blocks")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
space = (0, 0, 50)
point = 0

class Obstacle:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 80)
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def collide(self, player):
        return self.rect.colliderect(player.rect)

class Player:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 60, 60)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0 :  # Ліва межа
            self.rect.x -= self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0: # Ліва межа
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < 800:  # Права межа
            self.rect.x += self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800: # Права межа
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

class Score:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

    def collide(self, player):
        return self.rect.colliderect(player.rect)

    def increase(self, point):
        point += 1

creation = random.randint(0, 750)

mitiorites_1 = []
mitiorites_2 = []
mitiorites_3 = []
player = Player(375, 500)
score = []

obstacle_timer = 0
score_timer = 0

running = True
while running:

    obstacle_timer += 1
    score_timer += 1
    if obstacle_timer >= 60: # Кожну секунду (60 FPS)
        mitiorites_1.append(Obstacle(random.randint(0, 365), -50)) # Спочатку над екраном
        mitiorites_2.append(Obstacle(random.randint(376, 750), -50)) # Спочатку над екраном
        mitiorites_3.append(Obstacle(random.randint(0, 750), -50)) # Спочатку над екраном
        obstacle_timer = 0

    if score_timer >= 120:
        score.append(Score(random.randint(0, 750), -50)) # Спочатку над екраном
        score_timer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print()
        elif event == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player.rect.left > 0:  # Ліва межа
                player.rect.x -= player.speed
            if keys[pygame.K_LEFT] and player.rect.left > 0:  # Ліва межа
                player.rect.x -= player.speed
            if keys[pygame.K_d] and player.rect.right < 800:  # Права межа
                player.rect.x += player.speed
            if keys[pygame.K_RIGHT] and player.rect.right < 800:  # Права межа
                player.rect.x += player.speed

    screen.fill(space)
    player.draw(screen)
    player.update()
    for sc in score:
        sc.update()
        sc.draw(screen)
        if sc.rect.top > 600: # Якщо повністю за екраном
            score.remove(sc) # Видаляємо

    for ob in mitiorites_1:
        ob.update()
        ob.draw(screen)
        if ob.rect.top > 600: # Якщо повністю за екраном
            mitiorites_1.remove(ob) # Видаляємо

    for ob in mitiorites_2:
        ob.update()
        ob.draw(screen)
        if ob.rect.top > 600: # Якщо повністю за екраном
            mitiorites_2.remove(ob) # Видаляємо

    for ob in mitiorites_3:
        ob.update()
        ob.draw(screen)
        if ob.rect.top > 600:  # Якщо повністю за екраном
            mitiorites_3.remove(ob)  # Видаляємо

    pygame.draw.rect(screen, (255, 0, 0), player.rect, 2)  # Червона рамка

    pygame.display.flip() # Оновлюємо екран
    clock.tick(60) # 60 FPS

pygame.quit()
exit()