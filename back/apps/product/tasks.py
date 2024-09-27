from datetime import datetime, timedelta, timezone


from celery import shared_task
import json




ten_seconds = datetime.now(timezone.utc) + timedelta(seconds=10)

results = {}


i = [2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
8, 8, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 23, 23, 23, 23, 23, 23, 23,
23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23]
# TODO: НАстройть периодичность исполнения этой функции
# analyze_products_views.delay(ids)


@shared_task
def analyze_products_views_by_ids(ids):
    results['date'] = {}
    results['date']['hour'] = datetime.now(timezone.utc).now().isoformat()

    unique_ids = set(ids)
    for id in unique_ids:
        results['date'][f'{id}'] = ids.count(id)
    print('ANALYZE IDS', results)
    with open('data.json', 'a') as file:
        json.dump(results, file)
        # сохранять результаты в postgresql или orm django
    # return results