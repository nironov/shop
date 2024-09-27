from django.shortcuts import render
from django.views import View
from django.core.cache import cache
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.http import HttpRequest

from datetime import datetime, timedelta, timezone
import json
import os

from .tasks import analyze_products_views_by_ids


ten_seconds = datetime.now(timezone.utc) + timedelta(seconds=10)

i = [2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
8, 8, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 23, 23, 23, 23, 23, 23, 23,
23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23]


class ProductPageView(View):
    counts = []

    def count_product_views(self, request):
        product_id = int(request.path.split('/')[-1])
        self.counts.append(product_id)
        print('FROM QWE', self.counts)

        if len(self.counts) == 10:
            analyze_products_views_by_ids(self.counts)

            self.counts.clear()


    def get(self, request, product_id):
        self.ids = self.count_product_views(request)
        return render(request, 'product_page.html')

