from django.contrib import admin
from django.urls import path
from hero.views import HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hero/', HeroListView.as_view(), name='hero-list'),
    path('hero/<int:pk>/', HeroDetailView.as_view(), name='hero-detail'),
    path('hero/add/', HeroCreateView.as_view(), name='hero-add'),
    path('hero/<int:pk>/edit/', HeroUpdateView.as_view(), name='hero-edit'),
    path('hero/<int:pk>/delete/', HeroDeleteView.as_view(), name='hero-delete'),
]
