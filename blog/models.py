from tkinter import CASCADE
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts", default='')
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="posts", null=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    content = models.TextField(default='', validators=[MinLengthValidator(10)])
    excerpt = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.title} - {self.author} ({self.date}): {self.excerpt}"
