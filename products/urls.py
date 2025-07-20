from django.urls import path
from .views import *

urlpatterns = [
    path('', News_list.as_view(), name='news_list'),
    path('category/<int:pk>/', by_category, name='news_by_category'),
    path('detail/<int:pk>/', detail, name='news_detail'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('create/', Create.as_view(), name='create'),
    path('delete/<int:pk>//', Delete.as_view(), name='delete'),
    path('contact/', contact, name='contact')

]