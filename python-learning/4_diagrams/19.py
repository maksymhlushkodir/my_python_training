import matplotlib.pyplot as plt
import pandas as pd

товари = []
кількість = []
ціна = []
colors = ['#8B0000','#FFD700','#AA336A','#FFA500']
explode = [0.1, 0.1, 0.1, 0.1]

# КОМЕНТИ!!!!!!

# Складаємо шлях

with open('../5_file-assets/1_file_txt/for_diagrams/товари.txt', 'r', encoding='utf-8') as file:
    for line in file :
        parts = line.strip().split()
        if len(parts) == 3:
            товари.append(parts)
            кількість.append(int(parts[1])) # Перетворюємо в число
            ціна.append(int(parts[2]))

print("Товари:", товари)
print("Кількість:", кількість)
print("Ціна:", ціна)

# КОМЕНТИ!!!!!!

plt.pie(
    кількість,
    labels=товари,
    shadow=True,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=explode
)
plt.title('Кількість товарів на складі')
plt.show()

plt.bar(товари, ціна, color=colors[0])
plt.title('Ціна товарів')
plt.xlabel('Ціна (грн)')
for index, value in enumerate(ціна):
    plt.text(value, index, f'{value} грн' , va='center')

plt.tight_layout()  # Щоб нічого не обрізалося
plt.show()