from django.contrib import admin
from django.urls import path
from hero.views import (
    HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView, export_heroes,
    SignUpView, homeView, PageView, DocumentView,
    ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, export_articles,
    InvestigatorListView, InvestigatorCreateView, InvestigatorDetailView, InvestigatorUpdateView, InvestigatorDeleteView,
    PhotoCreateView, PhotoListView, PhotoDetailView, PhotoDeleteView, PhotoUpdateView, PhotoCarouselView,
    )
from django.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

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
    path('<str:page>.html', PageView.as_view(), name='Page'),
    path('<str:doc>.md', DocumentView.as_view(), name='Document'),
    path('investigator/', InvestigatorListView.as_view(), name='investigator-list'),
    path('investigator/add/', InvestigatorCreateView.as_view(), name='investigator-add'),
    path('investigator/<int:pk>/', InvestigatorDetailView.as_view(), name='investigator-detail'),
    path('investigator/<int:pk>/edit/', InvestigatorUpdateView.as_view(), name='investigator-edit'),
    path('investigator/<int:pk>/delete/', InvestigatorDeleteView.as_view(), name='investigator-delete'),
    path('hero/export/<str:file_format>/', export_heroes, name='export_heroes'),
    path('article/export/<str:file_format>/', export_articles, name='export_articles'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo-add'),
    path('photo/', PhotoListView.as_view(), name='photo-list'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
    path('photo/<int:pk>/edit/', PhotoUpdateView.as_view(), name='photo-edit'),
    path('photo/carousel/', PhotoCarouselView.as_view(), name='photo-carousel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
