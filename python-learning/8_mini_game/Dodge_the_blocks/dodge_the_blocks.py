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

class Button:

    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect((x, y,), (width, height))
        self.color = color
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def is_clicked(self, mouse_pos):
        return  self.rect.collidepoint(mouse_pos)

creation = random.randint(0, 750)

rezero_button = Button(300, 400, 200, 60, "Restart", (51, 51, 204))
mitiorites_1 = []
mitiorites_2 = []
mitiorites_3 = []
player = Player(375, 500)
score = []

obstacle_timer = 0
score_timer = 0
score_point = 0

game_active = True  # Початковий стан

def draw_game_over_screen(final_score):
    while not game_active:  # Поки гра на паузі
        mouse_pos = pygame.mouse.get_pos()
        screen.fill((0, 0, 0, 128))  # Напівпрозорий чорний фон
        draw_text = font.render("GAME OVER", True, (255, 255, 255))
        draw_text_score = font.render(f"points: {final_score}", True, (255, 255, 255))
        screen.blit(draw_text, (50, 50))
        screen.blit(draw_text_score, (50, 80))

        rezero_button.draw(screen)  # Малюємо кнопку

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rezero_button.is_clicked(mouse_pos):
                    print("click is found")
                    return True  # Повертаємо сигнал для рестарту
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True

        pygame.display.flip()
    return False

time_game = 0
time_game_in_seconds = 0

running = True
while running:

    if game_active:
        obstacle_timer += 1
        score_timer += 1

        time_game += 1
        if time_game >= 60:
            time_game_in_seconds += 1
            time_game = 0

        if obstacle_timer >= 60:  # Кожну секунду (60 FPS)
            mitiorites_1.append(Obstacle(random.randint(0, 365), -50))  # Спочатку над екраном
            mitiorites_2.append(Obstacle(random.randint(376, 750), -50))  # Спочатку над екраном
            mitiorites_3.append(Obstacle(random.randint(0, 750), -50))  # Спочатку над екраном
            obstacle_timer = 0

        if score_timer >= 120:
            score.append(Score(random.randint(0, 750), -50))  # Спочатку над екраном
            score_timer = 0

        text_score =  font.render(f"time game: {time_game_in_seconds}", True, (255, 255, 255))  # Текст білому кольору
        text_time = font.render(f"time game: {time_game_in_seconds}", True, (255, 255, 255))  # Текст білому кольору
        screen.blit(text_time, (50, 50))  # Координати (x, y)
        #screen.blit(text_time,
        screen.fill(space)
        player.draw(screen)
        player.update()



        for sc in score:
            sc.update()
            sc.draw(screen)
            if sc.rect.top > 600:  # Якщо повністю за екраном
                score.remove(sc)  # Видаляємо
            if sc.collide(player):
                score_point += 1
                score.remove(sc) # Видаляємо

        for ob in mitiorites_1:
            ob.update()
            ob.draw(screen)
            if ob.rect.top > 600:  # Якщо повністю за екраном
                mitiorites_1.remove(ob)  # Видаляємо
            if ob.collide(player):
                game_active = False

        for ob in mitiorites_2:
            ob.update()
            ob.draw(screen)
            if ob.rect.top > 600:  # Якщо повністю за екраном
                mitiorites_2.remove(ob)  # Видаляємо
            if ob.collide(player):
                game_active = False

        for ob in mitiorites_3:
            ob.update()
            ob.draw(screen)
            if ob.rect.top > 600:  # Якщо повністю за екраном
                mitiorites_3.remove(ob)  # Видаляємо
            if ob.collide(player):
                game_active = False

        pygame.draw.rect(screen, (255, 0, 0), player.rect, 2)  # Червона рамка

    else:
        #Малюємо екран Game Over
        draw_game_over_screen(score_point)

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

    pygame.display.flip() # Оновлюємо екран
    clock.tick(60) # 60 FPS

pygame.quit()
exit()