from django.contrib import admin
from .models import *



class NewsAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'user', 'created_at']
    list_filter = ['category', 'user']
    search_fields = ['title__icontains']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'info', 'user', 'created_at', 'email']
    list_filter = ['name', 'user']
    search_fields = ['name__icontains']

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comments)
