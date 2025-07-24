class Hero:
    def __init__(self, name): # Конструктор (як у Java, але __init__)
        self.name = name      # Публічна властивість
        self._health = 100    # "Захищена" (по конвенції)

    def attack(self):         # Метод
        print(f"{self.name} атакує!")
