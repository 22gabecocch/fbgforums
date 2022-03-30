from django.contrib import admin
from .models import Thread, Post, Category, Profile

admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Profile)