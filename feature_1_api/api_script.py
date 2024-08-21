import requests
import json


# URL API
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Подключение к API и получение данных
    response = requests.get(url)

    # Проверка статуса ответа
    if response.status_code == 200:
        # Получаем данные в формате JSON
        data = response.json()

        # Сохранение данных в файл
        with open('feature_1_api/posts.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        print("Данные успешно сохранены в файл posts.json.")
    else:
        print(f"Ошибка при подключении к API: {response.status_code}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
