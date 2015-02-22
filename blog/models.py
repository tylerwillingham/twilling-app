from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(max_length=70, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['slug']


class Category(models.Model):
    title = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(max_length=70, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['slug']


class Post(models.Model):
    title = models.CharField(max_length=125, unique=True)
    slug = models.SlugField(max_length=125, unique=True)
    status = models.ForeignKey('Status')
    categories = models.ManyToManyField('Category', blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
