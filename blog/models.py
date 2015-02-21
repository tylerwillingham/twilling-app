from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField(max_length=125)
    status = models.ForeignKey('Status')
    categories = models.ManyToManyField('Category')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
