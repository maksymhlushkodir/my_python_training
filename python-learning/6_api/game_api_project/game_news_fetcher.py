# Data obtained from the RAWG API (https://rawg.io/apidocs)

import requests
import os
import json
from dotenv import load_dotenv

try:
    import requests
except ImportError:
    print("Бібліотека 'requests' не встановлена. Спробуйте: pip install requests")
    input("exit")
    exit()

load_dotenv() # Завантажує змінні з .env файлу
API_KEY = os.getenv("RAWG_API_KEY")  # Ключ у файлі .env

while True:
    user_choice = input("[1. find the game / 2. read the .json file / 3. exit]\n:")

    if user_choice == '1':
        game_name = input("Введіть назву гри:").strip()
        if not game_name:
            print("❗ Назва гри не може бути пустою!")
            continue

        # Робимо запит до API
        url = f"https://api.rawg.io/api/games?key={API_KEY}&search={game_name}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json() # Отримуємо JSON

            if data['count'] > 0: #Якщо є результати
                game = data['results'][0] # Беремо першу гру

                game_info = {
                    # Отримуємо дані (можуть бути відсутні, тому обережно)
                    "name" : game.get("name", "Немає даних"),
                    "rating" : game.get("rating", "Немає даних"),
                    "released" : game.get("released", "Немає даних"),
                    # Розробники (перший у списку)
                    "developers" : developers[0]['name'] if (developers := game.get("developers", [])) else "Немає даних",
                    # Платформи (список)
                    "platforms" : [p['platform']['name'] for p in platforms ] if (
                    platforms := game.get("platforms", [])) else ["Немає даних"]
                }

                #відображаємо красивіше і зрозуміліше
                def print_game_info(info):
                    print(f"\n📜 Інформація про гру: {game_info['name']}")
                    print(f"⭐ Рейтинг: {game_info['rating']}")
                    print(f"📅 Дата виходу: {game_info['released']}")
                    print(f"👨‍💻 Розробник: {game_info['developers']}")
                    print(f"🎮 Платформи: .join{game_info['platforms']}") # .join для більш читабельності

                print_game_info(game_info)

            else:
                print("🔍 Гру не знайдено! Спробуйте іншу назву.")

        elif response.status_code == 404:
            print("🌐 Помилка: API не знайдено (404)")
        else:
            print(f"🌐 Помилка API: {response.status_code}")

        # зберігання даних ігри
        user_save = input("[1. load data / 2. repeat / 3. exit]\n:")

        if user_save == '1':
            user_file_name = input("name the file\n:")

            with open(f"../../5_file-assets/3_file_json/for_gameNews/{user_file_name}.json", 'w', encoding='utf-8') as file :
                # ensure_ascii=False для коректного відображення кирилиці
                json.dump(game_info, file, ensure_ascii=False, indent=4)
                print("the data has been saved")

        elif user_save == '2':
            print()

        elif user_choice == '3':
            exit()

        else:
            print("Error")

    elif user_choice == '2':
        user_file_name_r = input("Write the name of the file: ")  # Назва без розширення
        try:
            with open(f"../../5_file-assets/3_file_json/for_gameNews/{user_file_name_r}.json", 'r', encoding='utf-8') as file_r:
                file_content = file_r.read()  # Читаємо весь вміст
                print(file_content)  # Виводимо вміст
        except FileNotFoundError:
            print("😱 Файл не знайдено! Перевір назву або шлях.")
        except Exception as e:
            print(f"🚨 Помилка: {e}")

    elif user_choice == '3':
        exit()

    else:
        print("Error")