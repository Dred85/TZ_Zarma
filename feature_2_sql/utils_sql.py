import psycopg2


def create_db():
    """ ПОдключаемся к базе данных и создаем таблицу с данными"""
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="qwertyuiop123#",
        port="5432"
    )

    cursor = conn.cursor()

    # Создаем таблицу users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER
    )
    ''')

    # Добавляем некоторые данные
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Alice', 28))
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Bob', 34))
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Charlie', 25))
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('David', 40))

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    cursor.close()
    conn.close()
