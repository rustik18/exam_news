from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='log_in')
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')