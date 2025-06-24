import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Дані
films = ["Форсаж 9", "Дюна", "Оппенгеймер", "Барбі", "Титанік"]
ratings = [6.5, 8.0, 8.5, 7.3, 9.2]
years = [2021, 2021, 2023, 2023, 1997]

# Створення DataFrame
df = pd.DataFrame({
    'Фільм': films,
    'Рейтинг': ratings,
    'Рік': years
})

# Додавання категорій рейтингу
df['Категорія'] = np.where(df['Рейтинг'] >= 8.0, 'Високий', 'Середній')

# Пошук фільму з найвищим рейтингом
top_film = df.loc[df['Рейтинг'].idxmax(), 'Фільм']

# Вивід даних
print("--- Дані про фільми ---")
print(df)
print("\nФільм з найвищим рейтингом:", top_film)

# Візуалізація (горизонтальна стовпчикова діаграма)
df.plot(
    x='Фільм',
    y='Рейтинг',
    kind='barh',
    title='Рейтинги фільмів',
    legend=False,
    color='violet'
)

plt.tight_layout()
plt.show()