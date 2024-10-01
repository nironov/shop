from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View

from apps.core.postgresql_connection import cur
from .queries import get_filtered_products_from_db, get_product_by_search


# def product_page(request, product_id):

#     return render(request, 'product_page.html')

def add_to_cart(request):
    pass


class CatalogPageView(View):
    template_name = 'catalog.html'

    def get(self, request):
        cur.execute('select * from products')
        all_products = cur.fetchall()

        page_number = request.GET.get('page')
        qty_per_page = request.GET.get('quantity')
        paginator = Paginator(all_products, 9)
        context = {}

        # print('CACHED VALUE', cache.get('my_key'))

        filters: dict = dict(request.GET) # {'price-min': ['105'], 'price-max': ['515'], 'category': ['all'], 'brands': ['all'], 'quantity': ['9']}

        if filters and len(filters) > 1:
            filtered_products = get_filtered_products_from_db(filters)
            qty_per_page = request.GET.get('quantity')
            paginator = Paginator(filtered_products, qty_per_page)
            context['products'] = paginator.get_page(page_number)
            return render(request, self.template_name, context)

        if not filters or len(filters) == 1:
            if filters.get('q'):
                product = get_product_by_search(filters['q'][0])
                context['product'] = product
                return render(request, self.template_name, context)
            products = paginator.get_page(page_number)
            context['products'] = products
            return render(request, self.template_name, context)
