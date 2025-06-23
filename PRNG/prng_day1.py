import random

random.seed(123)  # задаємо однаковий seed
print("Перший запуск:")
print(random.randint(1, 100))
print(random.randint(1, 100))

random.seed(123)  # знову той самий seed
print("\nДругий запуск (має бути те саме):")
print(random.randint(1, 100))
print(random.randint(1, 100))