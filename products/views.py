from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required



class News_list(View):
    def get(self, request):
        query_t = request.GET.get('t', '')
        query_d = request.GET.get('d', '')
        categories = Category.objects.all()
        if query_t and query_d:
            news =News.objects.filter(
                Q(title__icontains=query_t) & Q(desc__icontains=query_d))
        elif query_t:
            news = News.objects.filter(Q(title__icontains=query_t))
        elif query_d:
            news = News.objects.filter(Q(desc__icontains=query_d))
        else:
            news = News.objects.all().order_by('-id')
        return render(request, 'blog/news_list.html', {'news_list': news,'categories': categories})




def by_category(request, pk):
    news_list = News.objects.filter(category_id=pk)
    categories = Category.objects.all()

    return render(request, 'blog/news_list.html', {
        'news_list': news_list,
        'categories': categories
    })



def detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = Comments.objects.filter(news=news)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.user = request.user
            comment.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'news': news, 'comments': comments,'form': form})







class Update(View):
    def get(self, request, pk):
        news = get_object_or_404(News, id=pk)
        form = NewsForm(instance=news)
        return render(request, 'blog/update.html', {'form': form, 'news': news})

    def post(self, request, pk):
        news = get_object_or_404(News, id=pk)
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_detail', news.id)
        return render(request, 'blog/update.html', {'form': form, 'news': news})


class Create(View):
    def get(self, request):
        form = NewsForm()
        return render(request, 'blog/create.html', {'form': form})

    def post(self, request):
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            news.save()
            return redirect('news_list')
        return render(request, 'blog/create.html', {'form': form})



class Delete(View):
    def post(self, request, pk):
        news = get_object_or_404(News, id=pk)
        if request.method == 'POST':
            news.delete()
            return redirect('news_list')

    def get(self, request, pk):
        news = get_object_or_404(News, id=pk)
        return render(request, 'blog/delete.html', {'news': news})


# views.py
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='log_in')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('contact')  # or a thank-you page
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})



