from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main.views import index

from blog.views import post_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('post/', post_view),
    path('tinymce/', include('tinymce.urls')),
]
if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)