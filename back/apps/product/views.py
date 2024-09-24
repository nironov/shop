from django.shortcuts import render
from django.views import View

from datetime import datetime, timedelta, timezone


ten_seconds = datetime.now(timezone.utc) + timedelta(seconds=10)

# Create your views here.

class ProductPageView(View):
    counts = []

    def count_product_views(self, request):
        product_id = int(request.path.split('/')[-1])
        self.counts.append(product_id)
        print(self.counts)
        return self.counts

    def get(self, request, product_id):
        return render(request, 'product_page.html')