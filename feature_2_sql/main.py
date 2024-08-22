from feature_2_sql.utils_sql import create_db
from feature_2_sql.sql_script import sql_query_for_selection

# Решение задания №2 с использованием БД PostgreSQL
def main():
    """Основные функции нашего скрипта:
        1. создает таблицу в существующей базе данных PostgreSQL
        2. выполняет SQL-запрос для вывода информации о пользователях старше 30 лет"""
    create_db()
    sql_query_for_selection()



if __name__ == "__main__":
    main()