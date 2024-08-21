import pandas as pd

# Загрузка данных из CSV и JSON
def merge_products():
    """ выводим итоговую таблицу с информацией о продажах для каждого продукта."""

    sales = pd.read_json('sales.json')
    products = pd.read_csv('products.csv')

    # Объединение данных по product_id
    merged_data = pd.merge(products, sales, on='product_id', how='left')

    # Вывод итоговой таблицы
    print(merged_data)

if __name__ == "__main__":
    merge_products()
