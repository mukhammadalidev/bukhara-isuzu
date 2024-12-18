from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, about_view,aksiya_view,aksiya_detail_view
from django.conf.urls.i18n import i18n_patterns  # i18n_patterns importi

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),

]

# i18n URL'lar uchun maxsus yo'llar
urlpatterns += i18n_patterns(  # i18n_patterns bilan URL'lar qo'shish
    path('i18n/', include('django.conf.urls.i18n')),  # i18n URL'ni qo'shish
    path('', index, name='home'),
    path('about/', about_view, name='about'),
    path('aksiys/',aksiya_view,name="aksiys"),
    path('aksiys/<int:id>/',aksiya_detail_view,name="aksiy_detail"),
    path('products/', include('products.urls')),
    path('news/', include('news.urls')),
)

# Faqat DEBUG rejimida statik va media fayllarni serverlash
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
