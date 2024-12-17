from django.urls import path
from .views import product_detail,category_detail,product_view

app_name = "product"

urlpatterns = [
    path('detail/<slug:slug>/',product_detail,name="detail"),
    path('category_detail/<int:id>/',category_detail,name="category-detail"),
    path('products/',product_view,name="products"),
]