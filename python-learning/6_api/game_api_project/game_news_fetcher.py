# Data obtained from the RAWG API (https://rawg.io/apidocs)

import requests
import os
import json
from dotenv import load_dotenv

try:
    import requests
except ImportError:
    print("Бібліотека 'requests' не встановлена. Спробуйте: pip install requests")
    exit()

load_dotenv() # Завантажує змінні з .env файлу
API_KEY = os.getenv("RAWG_API_KEY")  # Ключ у файлі .env
game_name = input("Введіть назву гри:").strip()

# Робимо запит до API
url = f"https://api.rawg.io/api/games?key={API_KEY}&search={game_name}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json() # Отримуємо JSON

    if data['count'] > 0: #Якщо є результати
        game = data['results'][0] # Беремо першу гру

        # Отримуємо дані (можуть бути відсутні, тому обережно)
        rating = game.get("rating", "Немає даних")
        released = game.get("released", "Немає даних")

        # Розробники (перший у списку)
        developers = game.get("developers", [])
        developer = developers[0]['name'] if developers else "Немає даних"

        # Платформи (список)
        platforms = game.get("platforms", [])
        platform_names = [p['platform']['name'] for p in platforms] if platforms else ['Немає даних']

        # Виводимо інформацію
        print(f"\nІнформація про гру '{game['name']}':")
        print(f"🔹 Рейтинг: {rating}")
        print(f"🔹 Дата виходу: {released}")
        print(f"🔹 Розробник: {developer}")
        print("🔹 Платформи:")
        for name in platform_names:
            print(f"   - {name}")

    else:
        print("Error: Гру не знайдено ")
else:
    print(f"Помилка запиту: {response.status_code}")