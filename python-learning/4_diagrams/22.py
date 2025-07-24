import matplotlib.pyplot as plt

games = ['Minecraft', 'GTA 5', 'CS2']
ratings = [95, 90, 85]
players = [150_000_000, 100_000_000, 50_000_000]

explode = [0.1,0.1,0.1]
colors = ['#008B8B', #Dark cyan (green)
          '#6D8196', #Slate gray (gray)
          '#F2B949'] #Mimosa (orange)

# Створюємо фігуру з 2 субплотами (1 рядок, 2 стовпці)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) # figsize - розмір вікна

# Діаграма 1: Рейтинги ігор (лівий графік)

ax1.bar(games, ratings, color='red')
ax1.set_title('Рейтинги ігор')
ax1.set_ylabel("Оцінка (з 100)")

# Діаграма 2: Кількість гравців (правий графік)

ax2.pie(
    players,
    labels=games,
    colors=colors,
    shadow=True,
    explode=explode,
    autopct='%1.1f%%',
    startangle=90
)
ax2.set_title("Кількість гравців")

# Загальний заголовок
plt.suptitle("Аналіз ігор 2024", fontsize=16) # fontsize - розмір текста

# Автоматичне розміщення, щоб не накладалося
plt.tight_layout()
plt.show()