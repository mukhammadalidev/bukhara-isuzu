from django.urls import path
from .views import news_detail,news_view

app_name = "news"
urlpatterns =[
    path('',news_view,name="news_all"),
    path('news/<int:id>/',news_detail,name="news_detail"),
]