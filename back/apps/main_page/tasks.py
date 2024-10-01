from celery import shared_task
from requests import get

@shared_task
def get_popular_products() -> dict[list[dict]]:
    products = get('http://127.0.0.1:8000/api/get_data').json()
    print('GET POP PRODUCTS', products, type(products))
    return products