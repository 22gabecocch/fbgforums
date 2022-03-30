from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
from datetime import date

class Profile(models.Model):
    """Model extending user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    

class Thread(models.Model):
    """Model representing a thread"""
    title = models.CharField(max_length=200, help_text='Enter thread title')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    post_date = models.DateTimeField()
    updated = models.DateTimeField()
    
class Post(models.Model):
    """Model representing a post"""
    thread = models.ForeignKey('Thread', on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    contents = models.CharField(max_length=1000, help_text='Enter post contents')

class Category(models.Model):
    """Model representing a category"""
    name = models.CharField(max_length=25, help_text='Enter category name')

