import matplotlib.pyplot as plt

games = ['DOOM', 'Minecraft', 'CupHead', 'ASTRO-bot', 'Hollow Knight']
hours = [65, 102, 40, 30, 172]

plt.pie(hours, labels=games, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Hours_on_games")
plt.show()