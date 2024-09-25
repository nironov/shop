from .views import ProductPageView
from .tasks import analyze_products_views

ids = ProductPageView.counts
print("IDS", ids)

print(analyze_products_views.apply_async(args=[ids], countdown=10))