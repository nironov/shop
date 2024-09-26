from django.shortcuts import render
from django.views import View
from django.core.cache import cache
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from datetime import datetime, timedelta, timezone

from .tasks import analyze_products_views

ten_seconds = datetime.now(timezone.utc) + timedelta(seconds=10)

i = [2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
8, 8, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 23, 23, 23, 23, 23, 23, 23,
23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23]

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

# TODO сделать celery
    def get(self, request, product_id):
        self.count_product_views(request)
        task = analyze_products_views.apply_async(args=(i,), countdown=5)
        print(task)
        # cache.set('my_key', 'value of my key', 100)
        # print('FROM GET', self.count_product_views(request))
        # self.count_product_views(request)
        # print(analyze_products_views.apply_async(self.counts))
        return render(request, 'product_page.html', context={'task':task})
