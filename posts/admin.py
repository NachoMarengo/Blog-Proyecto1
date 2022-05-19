from turtle import pos
from django.contrib import admin
from .models import Autor, Categoria, Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Autor)