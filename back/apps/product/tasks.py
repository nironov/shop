from datetime import datetime, timedelta, timezone

from apps.core.postgresql_connection import cur, conn

from celery import shared_task
import json


results = {}

@shared_task
def analyze_products_views_by_ids(ids):
    results = {}
    results['time'] = datetime.now(timezone.utc).now().isoformat()
    results['ids'] = {}

    unique_ids = set(ids)
    for id in unique_ids:
        results['ids'][f'{id}'] = ids.count(id)
    print('ANALYZE IDS', results)

    ids_json = json.dumps(results)
    cur.execute(f"insert into productsviews (ids) values ('{ids_json}')")
    conn.commit()