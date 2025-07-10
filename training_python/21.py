# завдання 1

print("\n===завдання 1===\n")
top_games = ("The Witcher 4", "GTA 6", "Starfield")

print(type(top_games))
print(top_games)
print(top_games[1])
# top_games[0] = "Cyberpunk 2"
print(top_games[0])

# завдання 2
print("\n===завдання 2===\n")
tags = ["RPG", "Action", "RPG", "Open World", "Action", "Horror"]

unique_tags = set(tags)
print(type(unique_tags))
unique_tags.add("Adventure")
print(unique_tags)
unique_tags.discard("Horror")  # Навіть якщо "Horror" немає — код не зламається!
print(unique_tags)

# завдання 3
print("\n===завдання 3===\n")

library = {
    "The Witcher 3": 100,
    "Cyberpunk 2077": 85,
    "Elden Ring": 95
}
print(type(library))
print(library)

library["Baldur's Gate 3"] = 90 #
library["Cyberpunk 2077"] = 90

print(library)

library.pop("Elden Ring", None)  # Не викличе помилку, якщо гри немає

print(library)

print(library.keys())
print(library.values())

# завдання 4
print("\n===завдання 4===\n")

players = ["Alex", "Bohdan", "Alex", "Olena"]
unique_players = set(players)
fav_games = {player: input(f"Улюблена гра {player}: ") for player in unique_players}

print(fav_games)