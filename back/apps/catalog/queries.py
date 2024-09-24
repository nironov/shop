from apps.core.postgresql_connection import cur

def get_filtered_products_from_db(filters: dict):

    if filters['category'][0] == 'all' and filters['brands'][0] == 'all':
        cur.execute(
            f'select * from products where price between {filters['price-min'][0]} and {filters['price-max'][0]}'
        )
        products = cur.fetchall()
        return products

    elif filters['category'][0] != 'all' and filters['brands'][0] == 'all':
        cur.execute(
            f"select * from products where price between {filters['price-min'][0]} and {filters['price-max'][0]} and category = '{filters['category'][0]}'"
        )
        products = cur.fetchall()
        return products

    elif filters['category'][0] == 'all' and filters['brands'][0] != 'all':
        cur.execute(
            f"select * from products where price between {int(filters['price-min'][0])} and {int(filters['price-max'][0])} and brand = '{filters['brands'][0]}'"
        )
        products = cur.fetchall()
        return products


def get_product_by_search(product_name: str):
    cur.execute(
        f"select * from products where productname = '{product_name}'"
    )
    product = cur.fetchone()
    print('PRODUCT NAME', product)
    return product