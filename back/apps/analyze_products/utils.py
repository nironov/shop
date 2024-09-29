from apps.core.postgresql_connection import cur, conn


def get_most_viewed_products_from_db():
    try:
        cur.execute('select * from products_data where is_checked = False')
        data = cur.fetchone()
        cur.execute(f"update products_data set is_checked = True where id = {data[0]}")
        conn.commit()
    except Exception as e:
        print(e)

    print('DATA MOSI VIEWED FUNC', data)

# TODO: доработать алгоритм извелечения и анализа продуктов из БД
def get_most_viewed_products_by_id():
    pass