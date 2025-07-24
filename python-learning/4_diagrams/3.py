import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Дані
prices = [100, 55, 20]  # ціни товарів
items = ["salary", "adjustable dumbbell", "elastic bandage for hands"]  # назви

# Створюємо DataFrame
df = pd.DataFrame({
    'Item': items,       # стовпець з назвами товарів
    'Price': prices      # стовпець з цінами
})

# Виводимо таблицю
print("--- Дані ---")
print(df)

# Візуалізація (стовпчикова діаграма)
df.plot(
    x='Item',           # вісь X — назви товарів
    y='Price',          # вісь Y — ціни
    kind='bar',         # тип графіка — стовпчики
    title='Витрати',    # заголовок
    legend=False,       # приховати легенду
    color='skyblue'     # колір стовпців
)

plt.xticks(rotation=45)  # повернути підписи на 45 градусів
plt.tight_layout()       # автоматичне розміщення елементів
plt.show()