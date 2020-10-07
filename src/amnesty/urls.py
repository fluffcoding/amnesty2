from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main.views import index, search

from blog.views import post_view, latest, category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('post/<slug>', post_view, name='post'),
    path('tinymce/', include('tinymce.urls')),
    path('latest/', latest, name='latest'),
    path('search/', search, name='search'),
    path('accounts/', include('allauth.urls'), name='allauth'),
    path('category/<id>', category, name='category'),
    path('team/', include('management.urls'), name='team')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)