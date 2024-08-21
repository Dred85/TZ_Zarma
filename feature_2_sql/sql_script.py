import psycopg2


def sql_query_for_selection():
    """ Делаем выборку пользователей старше 30 лет и выводим их имена и возраст."""

    # Подключаемся к базе данных и открываем курсор
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="qwertyuiop123#",
        port="5432"
    )

    cursor = conn.cursor()

    # SQL-запрос для выбора всех пользователей старше 30 лет
    query = "SELECT name, age FROM users WHERE age > %s"
    age_limit = 30

    try:
        # Выполняем запрос
        cursor.execute(query, (age_limit,))

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
    except psycopg2.Error as e:
        print(f"Ошибка при взаимодействии с базой данных: {e}")
    finally:
        # Закрываем соединение
        cursor.close()
        conn.close()


if __name__ == "__main__":
    sql_query_for_selection()
