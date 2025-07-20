import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figimage

games = []
ratings = []
colors = []
explode=[]

with open('../5_file-assets/1_file_txt/for_diagrams/ratings-games_2.txt', 'r', encoding='utf-8') as file_games_txt_r:
    for line in file_games_txt_r:
        line = line.strip() # Видаляємо зайві пробіли та \n
        if line : # Якщо рядок не порожній
            parts = line.split(',') # Розділяємо по комі\
            game_name = parts[0].strip() # Видаляємо пробіли навколо назви
            ratings_game = parts[1].strip() # Перетворюємо рейтинг в число
            games.append(game_name)
            ratings.append(ratings_game)

total_number = len(games) # скільки ігор є
max_ratings = max(ratings) # максимальний рейтинг
max_games = [games for games, ratings in zip(games, ratings) if ratings == max_ratings] # хз як це працює просто ctrl+C ctrl+V

while True:

    user_choice = input("1.add game / 2. next")

    if user_choice == '1':
        user_game_rating = input("name game ',' game rating ")
        with open('../5_file/0_file_txt/games2.txt', 'a', encoding='utf-8') as file_games_txt_a:
            file_games_txt_a.write("\n" + user_game_rating)

    elif user_choice == '2':
        break

    else:
        print("Error: command not found")

games = np.array(games)
ratings = np.array(ratings)

df = pd.DataFrame({
    'games' : games,
    'ratings' : ratings,
})
#===data===
print(df)
print(f"the highest rating(s) in the : {', '.join(max_games)} (rating(s): {max_ratings})")
print(f"{total_number} games in total")
#===for-beauty===
for rating_C_E in ratings:
    rating = int(rating_C_E)  # Перетворюємо на int перед порівнянням
    if rating > 90:
        colors.append('#008B8B')  # str() не потрібно, '#008B8B' вже рядок
        explode.append(0.1)       # float() не обов'язково, 0.1 вже float
    elif rating > 70:
        colors.append('#EAA221')
        explode.append(0.1)
    else:
        colors.append('#B22222')
        explode.append(0.1)
#===matplotlib===
fig, (ax1, ax2 ) = plt.subplots(1,2, figsize=(12, 5)) # figsize - розмір вікна

#===1-bar===
ax1.bar(games, ratings, color='#6D8196')
ax1.set_title('game rating')
ax1.set_ylabel('ratings(0/100)')

#===2-pie===
ax2.pie(ratings, labels=games, startangle=90, shadow=True, colors=colors, autopct='%1.1f%%', explode=explode)
ax2.set_title('game rating')
#===plt===
plt.suptitle('game rating')
plt.tight_layout()
plt.show()