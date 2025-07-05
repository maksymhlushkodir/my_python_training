import matplotlib.pyplot as plt
# Ура коменти
language = ['python', 'java', 'C#']
hours_week = [7, 14, 21]

explode = [0.1, 0.1, 0.1] # Виділяємо ВСЕ!
colors = ['#006400','#FFDF00', '#551A8B'] # Гарні кольори

plt.pie(
    hours_week,
    labels=language,
    shadow=True,
    autopct='%1.1f%%',
    explode=explode,
    startangle=90,
    colors=colors
)

# Додаємо білу окружність  як "donut chart"
center_circle = plt.Circle((0, 0), 0.7, fc='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)
# кінець
plt.title('hours_week')
plt.show()