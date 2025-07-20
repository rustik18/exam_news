from django.shortcuts import render
from .models import *

def news_list(request):
    news_list = News.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/news_list.html', {'news_list': news_list,'categories': categories})
