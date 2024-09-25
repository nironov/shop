from django.shortcuts import render
from django.views import View

from datetime import datetime, timedelta, timezone

from .tasks import analyze_products_views

ten_seconds = datetime.now(timezone.utc) + timedelta(seconds=10)

# Create your views here.

class ProductPageView(View):
    counts = []

    # info = analyze_products_views.delay(counts)

    def count_product_views(self, request):
        product_id = int(request.path.split('/')[-1])
        self.counts.append(product_id)
        print('FROM QWE', self.counts)
        # res = analyze_products_views(self.counts)
        # print('RES FROM QWE', res)
        return self.counts

# TODO сделатьь celery
    def get(self, request, product_id):
        self.count_product_views(request)
        # print('FROM GET', self.count_product_views(request))
        # self.count_product_views(request)
        # print(analyze_products_views.apply_async(self.counts))
        return render(request, 'product_page.html')
