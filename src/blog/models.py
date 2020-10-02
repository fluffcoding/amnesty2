from django.db import models

from tinymce import models as tinymce_models


class Topic(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    slug = models.SlugField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    content = tinymce_models.HTMLField()
    topics = models.ManyToManyField(Topic, related_name='topics_name')
    image = models.ImageField(null=True, blank=True)