import matplotlib.pyplot as plt
from setuptools.command.rotate import rotate

games = []
ratings = []

with open('../5_file-assets/1_file_txt/for_diagrams/ratings-games_1.txt', 'r', encoding='utf-8') as file_r:
    for line in file_r:
        line = line.strip()
        if line:
            parts = line.split()
            game_name = ''.join(parts[:-1])
            rating = int(parts[-1])
            games.append(game_name)
            ratings.append(rating)


while True:
    user_choice = input("1.add game / 2.further")

    if user_choice == '1':
        add_game = input("game-name and game-estimates")
        with open('../5_file/0_file_txt/games.txt', 'a', encoding='utf-8') as file_a:
            file_a.write("\n" + add_game + "\n")
            games.append(add_game)

    elif user_choice == '2':
        break

    else:
        print("Error - you have uploaded data that cannot be disassembled")

colors = ['green' if good >=0 else 'red' for good in ratings]

plt.bar(games, ratings, color=colors)
plt.xlabel('game name')
plt.ylabel('rating')
plt.title('rating game')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()