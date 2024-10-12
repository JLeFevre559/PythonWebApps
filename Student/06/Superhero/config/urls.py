from django.contrib import admin
from django.urls import path
from hero.views import HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView, SignUpView
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
]
