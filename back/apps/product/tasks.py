from datetime import datetime, timedelta, timezone

from apps.core.postgresql_connection import cur, conn

from celery import shared_task
import json
from requests import get

# import redis
# red = redis.Redis()
# red.set('my_key', 'value of my key in redis')
# print(red.get('cli_key'))




results = {}

@shared_task
def put_viewed_products_in_db(ids):
    results = {}
    # results['time'] = datetime.now(timezone.utc).now().isoformat()
    results['data'] = {}
    # time = datetime.now(timezone.utc).now().isoformat()
    time = datetime.today()
    print('TIME', time)

    unique_ids = set(ids)
    for id in unique_ids:
        results['data'][f'{id}'] = ids.count(id)
    print('ANALYZE IDS', results)

    ids_json = json.dumps(results)

    # getting id of last record
    cur.execute('select id from products_data order by id desc')
    last_id = cur.fetchone()[0]
    print('LAST ID', last_id)

    # insert new data to DB
    cur.execute(f"insert into products_data (id, created_at, data, is_checked) values ({last_id + 1}, '{time}', '{ids_json}', False)")
    conn.commit()

    get('http://127.0.0.1:8000/api/get_data', data={'new_popular_products': True})

