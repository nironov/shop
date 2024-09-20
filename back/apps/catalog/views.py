from django.shortcuts import render

from apps.core.postgresql_connection import cur

def catalog_page(request):
    #TODO описать логику здесь
    # TODO добавить страницы инфо и контакты
    if request.method == 'GET':
        filters = dict(request.GET) # {'price-min': ['105'], 'price-max': ['515'], 'category': ['all'], 'brands': ['all'], 'quantity': ['9']}
        # filtered_products = # TODO написать sql запрос используя фильтры из URL строки

    return render(request, 'catalog.html')


def product_page(request, product_id):
    if product_id:
        print(product_id)
    return render(request, 'product_page.html')

def add_to_cart(request):
    pass
