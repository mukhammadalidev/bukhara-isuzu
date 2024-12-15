from django.shortcuts import render
from news.models import News
from products.models import Product,Category
from django.core.cache import cache

def index(request):
    # Redisdan ma'lumot olish
    news = cache.get('news')
    products = cache.get('products')
    category = cache.get('category')
    
    if not news:
        news = News.objects.all()[:]
        cache.set('news', news, timeout=3600)  # Keshga saqlash
    if not products:
        products = Product.objects.all()[:]
        cache.set('products', products, timeout=3600)  # Keshga saqlash

    if  not category:
        category = Category.objects.all()
    # Ma'lumotlarni contextga qo‘shish
    context = {
        "news": news,
        "products": products,
        "category":category
    }

    return render(request, 'index.html', context)
