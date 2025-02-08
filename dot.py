# import requests

# def get_player_matches(player_id):
#     url = f"https://api.opendota.com/api/players/{player_id}/recentMatches"
#     response = requests.get(url)
#     print(response.text)

#     if response.status_code == 200:
#         matches = response.json()
#         for match in matches[:5]:  # Выводим 5 последних игр
#             print(f"Матч ID: {match['match_id']}, Героем {match['hero_id']}, Убийства: {match['kills']}")
#     else:
#         print("Ошибка получения данных")

# # Пример для игрока (замените на нужный Steam ID)
# steam_id = "76561198972668781"
# print(get_player_matches(steam_id))

import requests

# # URL для получения данных о героях
# API_URL = "https://api.opendota.com/api/heroes"

# # Отправляем GET-запрос
# response = requests.get(API_URL)

# # Проверяем успешность запроса
# if response.status_code == 200:
#     heroes = response.json()
    
#     # Найдем героя по ID (например, Anti-Mage, ID = 1)
#     hero_id = 2
#     hero = next((h for h in heroes if h["id"] == hero_id), None)
    
#     if hero:
#         print(f"Герой: {hero['localized_name']}, Роль: {', '.join(hero['roles'])}")
#     else:
#         print("Герой не найден")
# else:
#     print("Ошибка запроса:", response.status_code)

# def get_hero_stats():
#     url = "https://api.opendota.com/api/heroStats"
#     response = requests.get(url)

#     if response.status_code == 200:
#         heroes = response.json()

#         # Найдем конкретного героя (например, Pudge)
#         hero = next((h for h in heroes if h["localized_name"] == "Pudge"), None)
#         if hero:
#             print(f"Герой: {hero['localized_name']}")
#             print(f"Средний винрейт: {hero['pro_win'] / hero['pro_pick']:.2%}")
#             print(f"Средний KDA: {hero['pro_pick']}")
#         else:
#             print("Герой не найден")
#     else:
#         print("Ошибка запроса:", response.status_code)

# get_hero_stats()


def get_recent_matches():
    url = "https://api.opendota.com/api/proMatches"
    response = requests.get(url)

    if response.status_code == 200:
        matches = response.json()
        for match in matches[:5]:  # Выведем 5 последних игр
            print(f"Матч ID: {match['match_id']}, Победила команда {match['radiant_win'] and 'Radiant' or 'Dire'}")
    else:
        print("Ошибка запроса:", response.status_code)

get_recent_matches()
