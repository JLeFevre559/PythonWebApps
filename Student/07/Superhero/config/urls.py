from django.contrib import admin
from django.urls import path
from hero.views import (
    HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView, 
    SignUpView, homeView,
    ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView)
from django.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hero/', HeroListView.as_view(), name='hero-list'),
    path('hero/<int:pk>/', HeroDetailView.as_view(), name='hero-detail'),
    path('hero/add/', HeroCreateView.as_view(), name='hero-add'),
    path('hero/<int:pk>/edit/', HeroUpdateView.as_view(), name='hero-edit'),
    path('hero/<int:pk>/delete/', HeroDeleteView.as_view(), name='hero-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', homeView.as_view(), name='home'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/add/', ArticleCreateView.as_view(), name='article-add'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-edit'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]
