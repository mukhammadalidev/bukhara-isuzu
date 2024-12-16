from django.shortcuts import render
from .models import News
# Create your views here.
def news_detail(request,id):

    news = News.objects.get(id=id)
    context = {
        "news":news
    }

    return render(request,'news_detail.html',context)