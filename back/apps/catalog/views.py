from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View

import asyncio

from apps.core.postgresql_connection import cur
from .queries import get_filtered_products_from_db

# def catalog_page(request):
#     if request.method == 'GET':
#         cur.execute('select * from products')
#         all_products = cur.fetchall()

#         paginator = Paginator(all_products, 10)
#         page_number = request.GET.get('page')
#         products = paginator.get_page(page_number)
#         # TODO: сформировать корректную url строку для get запроса с учетом фильтров

#         filters = dict(request.GET) # {'price-min': ['105'], 'price-max': ['515'], 'category': ['all'], 'brands': ['all'], 'quantity': ['9']}
#         if filters:

#             category_filter:int | str = int(filters['category'][0]) if filters['category'][0].isdigit() else 'all'
#             print('CATEGORY FILTER',category_filter, type(category_filter))
#             if category_filter.isdigit():
#                 cur.execute(
#                     f"select * from products where price between {int(filters['price-min'][0])} and {int(filters['price-max'][0])} and category = '{category_filter}' and brand = '{filters['brands'][0]}'")
#                 filtered_products = cur.fetchall()
#                 # print(filtered_products)
#                 return render(request, 'catalog.html', {'products': products})

#             cur.execute(
#                 f"select * from products where price between {int(filters['price-min'][0])} and {int(filters['price-max'][0])} and brand = '{filters['brands'][0]}' order by price")
#             filtered_products = cur.fetchall()
#             # print(filtered_products)
#             return render(request, 'catalog.html', {'products': products })
#     return render(request, 'catalog.html', {'products': products})


def product_page(request, product_id):

    return render(request, 'product_page.html')

def add_to_cart(request):
    pass


class CatalogPageView(View):
    template_name = 'catalog.html'

    def get_filters(self):
        q = self.request.GET.copy()
        q.pop(self.page_kwarg, None)
        print("URLENCODE", q.urlencode())
        return q.urlencode()

    def path_without_page(self):
        print("PATH WITHOUT PAGE", f'{self.request.path}?{self.get_filters()}')
        return f'{self.request.path}?{self.get_filters()}'

    async def get(self, request):
        cur.execute('select * from products')
        all_products = cur.fetchall()

        page_number = request.GET.get('page')
        qty_per_page = request.GET.get('quantity')
        paginator = Paginator(all_products, 10)
        products = paginator.get_page(page_number)
        context = {
            'msg': 'thisis message'
        }
        filters = dict(request.GET) # {'price-min': ['105'], 'price-max': ['515'], 'category': ['all'], 'brands': ['all'], 'quantity': ['9']}
        if not filters:
            print('NOT FILTERS', request.GET)
            context['products'] = products
            return render(request, self.template_name, context)

        else:
            # TODO: не доходит запрос к БД
            filtered_products = get_filtered_products_from_db(filters)
            print('FILTERED', filtered_products)
            context['products'] = filtered_products
            return render(request, self.template_name, context)