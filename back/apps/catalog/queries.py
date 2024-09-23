from apps.core.postgresql_connection import cur

def get_filtered_products_from_db(filters: dict):

    if filters['category'] == 'all' and filters['brands'] == 'all':
        cur.execute(
            f'select * from products where price between {filters['price_min']} and {filters['price_max']}'
        )
        products = cur.fetchall()
        print('1', products)
        return products

    elif filters['category'] != 'all' and filters['brands'] == 'all':
        cur.execute(
            f"select * from products where price between {filters['price_min']} and {filters['price_max']}and '{filters['category']}'"
        )
        products = cur.fetchall()
        print('2', products)
        return products

    elif filters['category'] == 'all' and filters['brands'] != 'all':
        cur.execute(
            f"select * from products where price between {filters['price_min']} and {filters['price_max']}and '{filters['brands']}'"
        )
        products = cur.fetchall()
        print('3', products)
        return products