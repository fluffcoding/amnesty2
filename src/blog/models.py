from django.db import models

from tinymce import models as tinymce_models


class Topic(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Post(models.Model):
    slug = models.SlugField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    content = tinymce_models.HTMLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Topic)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name