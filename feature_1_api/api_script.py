import requests
import json

from config_root import path_to_file_json_posts


# URL API
url = "https://jsonplaceholder.typicode.com/posts"

def main(url):
    """данный скрипт подключается к API, получает данные и записывает их в файл"""
    try:
        # Подключение к API и получение данных
        response = requests.get(url)

        # Проверка статуса ответа
        if response.status_code == 200:
            # Получаем данные в формате JSON
            data = response.json()

            # Сохранение данных в файл
            with open(path_to_file_json_posts, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4)

            print("Данные успешно сохранены в файл posts.json.")
        else:
            print(f"Ошибка при подключении к API: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main(url)
