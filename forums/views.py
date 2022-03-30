from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Thread, Post, Profile, Category
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    """View function for home page of site."""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class ProfileView(generic.base):
    """View function for user's profile."""
     