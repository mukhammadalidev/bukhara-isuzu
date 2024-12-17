from django.shortcuts import render
from .models import News
# Create your views here.


def news_view(request):
    news = News.objects.all()
    context = {
        "news":news
    }

    return render(request,'news.html',context)

def news_detail(request,id):

    news = News.objects.get(id=id)
    context = {
        "news":news
    }

    return render(request,'news_detail.html',context)