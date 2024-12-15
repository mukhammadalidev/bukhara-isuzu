from django.urls import path
from .views import product_detail,category_detail

app_name = "product"

urlpatterns = [
    path('detail/<slug:slug>/',product_detail,name="detail"),
    path('category_detail/<int:id>/',category_detail,name="category-detail")
]