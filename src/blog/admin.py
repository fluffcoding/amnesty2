from django.contrib import admin

from .models import Post, Topic, Category


admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Category)
