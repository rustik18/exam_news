from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# models.py
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    desc = models.TextField()
    image = models.ImageField(upload_to='news/', default='default/news.jpg', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        db_table = 'news'


class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rate = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.news.title

    class Meta:
        ordering = ['-created_at']
        db_table = 'comments'

class Contact(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email =  models.EmailField(blank=True, null=True)
    info = models.CharField(max_length=140, blank=True, null=True)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'contacts'

    def __str__(self):
        return self.name
