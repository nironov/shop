from django.shortcuts import render
from django.views import View
from django.core.cache import cache
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.http import HttpRequest

from datetime import datetime, timedelta, timezone
import json
import os

from .tasks import put_viewed_products_in_db


ten_seconds = datetime.now(timezone.utc) + timedelta(seconds=10)

i = [2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
8, 8, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 23, 23, 23, 23, 23, 23, 23,
23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23]


class ProductPageView(View):
    template_name = 'product_page.html'
    id_container = []

    def count_product_views(self, request):
        product_id = int(request.path.split('/')[-1])
        self.id_container.append(product_id)
        # исполнять эту проверку раз в сутки
        # celery beat  не подходит
        # TODO:  celery beat  не подходит. Найти другой способ
        if len(self.id_container) == 15:
            put_viewed_products_in_db(self.id_container)
            self.id_container.clear()


    def get(self, request, product_id):
        self.ids = self.count_product_views(request)
        return render(request, self.template_name)

