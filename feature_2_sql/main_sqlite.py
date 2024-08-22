import sqlite3

# Решение задания №2 с использованием БД SQLite
def main():
    """Основные функции нашего скрипта:
    1. создает таблицу в существующей базе данных SQLite
    2. выполняет SQL-запрос для вывода информации о пользователях старше 30 лет"""
    # Подключаемся к базе данных (если она не существует, она будет создана)


    conn = sqlite3.connect('users_30.db')
    cursor = conn.cursor()

    # Создаем таблицу users
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            age INTEGER)''')

    # Добавляем некоторые данные (необязательно)
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Кирилл', 31))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Мария', 20))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Александр', 38))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Глеб', 8))

    # Сохраняем изменения и закрываем соединение
    conn.commit()

    # SQL-запрос для выбора всех пользователей старше 30 лет
    query = "SELECT name, age FROM users WHERE age > 30"

    try:
        # Выполняем запрос
        cursor.execute(query)

        # Получаем все результаты
        results = cursor.fetchall()

        # Проверяем, есть ли результаты
        if results:
            print("Пользователи старше 30 лет:")
            for row in results:
                name, age = row
                print(f"Имя: {name}, Возраст: {age}")
        else:
            print("Пользователи старше 30 лет не найдены.")
    except sqlite3.Error as e:
        print(f"Ошибка при взаимодействии с базой данных: {e}")
    finally:
        # Закрываем соединение
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
