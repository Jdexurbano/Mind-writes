from django.contrib import admin
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','author','title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','blog', 'content')

# Register your models here.

admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)