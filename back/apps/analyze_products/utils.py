from apps.core.postgresql_connection import cur, conn


import redis
import json
import pickle


red = redis.Redis()

def get_ids_from_db():
    try:
        cur.execute('select * from products_data where is_checked = False')
        data = cur.fetchone()
        cur.execute(f"update products_data set is_checked = True where id = {data[0]}")
        conn.commit()
        print(data[2], type(data[2]))
        return data
    except Exception as e:
        print(e)


    print('IDS FROM DB FUNC', data)


def get_most_viewed_products_by_id() -> list[(tuple, tuple)]:
    products = get_ids_from_db()

    # {'1': 2, '4': 3, '6': 4, '9': 1}
    products_ids = products[2]['data']

    # [('2', 1), ('5', 1), ('6', 1), ('3', 2), ('7', 2), ('4', 3), ('1', 5)]
    sorted_ids_list = [(k, v) for k, v in sorted(products_ids.items(), key=lambda item: item[1])]

    # [('3', 2), ('7', 2), ('4', 3), ('1', 5)]
    four_most_popular_products = sorted_ids_list[-4:]

    most_viewed_products = [] # list[(tuple), (tuple), ...]
    for product_id in four_most_popular_products:
        cur.execute(f'select * from products where id = {product_id[0]}')
        most_viewed_products.append(cur.fetchone())
    print('POPULAR PRODUCTS', most_viewed_products)

    return most_viewed_products


def popular_products_in_list() -> list[dict]:

    data = get_most_viewed_products_by_id()

    data_in_list = []
    for product in data:
        data_in_list.append(
            {
                'id': product[0],
                'product_name': product[1],
                'price':  product[2],
                'description': product[3],
                'brand' :product[4],
                'category': product[5]
            }
        )


    red.set('products_data', pickle.dumps(data_in_list))

    """
        data_in_list
        [{'id': 3, 'product_name': 'product3', 'price': 690, 'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'brand': 'rowenta', 'category': '1'}, {'id': 7, 'product_name': 'product7', 'price': 890, 'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'brand': 'dyson','category': '2'}]
    """
    return data_in_list