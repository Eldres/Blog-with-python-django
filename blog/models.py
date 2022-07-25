from django.db import models

# Create your models here.

class Blog(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=50)
  date = models.DateField(auto_now_add=True)
  image = models.FileField()
  slug = models.SlugField(allow_unicode=True)
  content = models.TextField(default='')
  excerpt = models.CharField(max_length=150)

  def __str__(self):
    return f"{self.title} - {self.author} ({self.date}): {self.excerpt}"