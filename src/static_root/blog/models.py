from django.db import models

from tinymce import models as tinymce_models


class Post(models.Model):
    slug = models.SlugField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    content = tinymce_models.HTMLField()
    