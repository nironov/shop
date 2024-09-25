from datetime import datetime, timedelta, timezone

from config.celery import celery_app
from celery import shared_task

ten_seconds = datetime.now(timezone.utc) + timedelta(seconds=10)

results = {}


i = [2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
8, 8, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 23, 23, 23, 23, 23, 23, 23,
23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23]
# TODO: НАстройть периодичность исполнения этой функции
# analyze_products_views.delay(ids)

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, ids, **kwargs):
    sender.add_periodic_task(10, analyze_products_views.s(ids))



@celery_app.task
def analyze_products_views(ids):
    results['date'] = {}
    results['date']['hour'] = ''

    unique_ids = set(ids)
    for id in unique_ids:
        results['date'][id] = ids.count(id)
    print('ANALYZE IDS', results)
    return results