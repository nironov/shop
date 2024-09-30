from apps.core.postgresql_connection import cur, conn

# rename func
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

# TODO: доработать алгоритм извелечения и анализа продуктов из БД
def get_most_viewed_products_by_id():
    products = get_ids_from_db()

    products_ids = products[2]['data'] # {'1': 2, '4': 3, '6': 4, '9': 1}
    sorted_ids_list = [(k, v) for k, v in sorted(products_ids.items(), key=lambda item: item[1])] # [('2', 1), ('5', 1), ('6', 1), ('3', 2), ('7', 2), ('4', 3), ('1', 5)]
    four_most_popular_products = sorted_ids_list[-4:] # [('3', 2), ('7', 2), ('4', 3), ('1', 5)]
    # print('SORTED IDS', sorted_ids)
    print('SORTED IDS LIST', sorted_ids_list)
    print('four_most_popular_products', four_most_popular_products)

    most_viewed_products = [] # list[(tuple), (tuple), ...]
    for product_id in four_most_popular_products:
        cur.execute(f'select * from products where id = {product_id[0]}')
        most_viewed_products.append(cur.fetchone())
    print('POPULAR PRODUCTS', most_viewed_products)

    return most_viewed_products

def format_popular_products_to_dict():
    data = get_most_viewed_products_by_id()
    data_in_dict = {
        'data': []
    }
    print('DATA IN DICT', data_in_dict)
    for product in data:
        data_in_dict['data'].append(
            {
                'id': product[0],
                'product_name': product[1],
                'price':  product[2],
                'description': product[3],
                'brand' :product[4],
                'category': product[5]
            }
        )
    print("DATA IN DICT", data_in_dict)