from django.shortcuts import render
from news.models import News
from products.models import Product,Category
from news.models import Aksiya
from django.core.cache import cache

def index(request):
    # Redisdan ma'lumot olish
    news = cache.get('news')
    products = cache.get('products')
    category = cache.get('category')
    
    if not news:
        news = News.objects.all()[:4]
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



def about_view(request):
    return render(request,'about.html')



def aksiya_view(request):
    aksiya = Aksiya.objects.all()
    return render(request,'Aksiya.html',
                  context={
                      "aksiys":aksiya
                  }
                  )


def aksiya_detail_view(request,id):
    aksiya = Aksiya.objects.get(id=id)
    return render(request,'aksiya_detail.html',context={"aksiya":aksiya})





def services_view(request):
    return render(request,'services.html')