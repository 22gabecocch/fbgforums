from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.SearchView.asView(), name='search'),
    path('catsearch', views.CategorySearchView.asView(), name='catsearch'),
    path('tagsearch', views.TagSearchView.asView(), name='tagsearch'),
    path('profile', views.ProfileView.asView(), name='profile'),

]