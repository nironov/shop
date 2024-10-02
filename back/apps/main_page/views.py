from django.shortcuts import render
from django.views import View

from requests import get

from .tasks import get_popular_products


# def index_page(request):
#     return render(request, 'index.html', {'m':'mee123'})

class IndexPageView(View):
    template_name = 'index.html'

    def get(self, request):
        # из другой функции получать обьект, который содержит популярные товары
        q_products = get('http://127.0.0.1:8000/api/get_data', data={'get_popular_products': True}).json()
        print('PRODUCTS INDEX PAGE GET', q_products['data'], type(q_products['data']))

        products = []

        for product in q_products['data']:
            products.append(product)
        print('JUST PRODUCTS', products)
        return render(request, self.template_name, {'products': products})