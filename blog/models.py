from tkinter import CASCADE
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts", default='')
    date = models.DateField(auto_now=True)
    # image = models.FileField()
    image_name = models.CharField(max_length=100, default='')
    slug = models.SlugField(unique=True, allow_unicode=True)
    content = models.TextField(default='', validators=[MinLengthValidator(10)])
    excerpt = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.title} - {self.author} ({self.date}): {self.excerpt}"
