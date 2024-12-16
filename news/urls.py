from django.urls import path
from .views import news_detail

app_name = "news"
urlpatterns =[
    path('news/<int:id>/',news_detail,name="news_detail")
]