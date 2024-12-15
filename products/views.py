from django.shortcuts import render
from .models import Product,Category


def product_detail(request,slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    print(products)
    context = {
        "products":products
    }

    return render(request,"detail.html",context=context)


def category_detail(request,id):
    product = Product.objects.get(id=id)

    context = {
        "product":product
    }

    return render(request,'detail_product.html',context)