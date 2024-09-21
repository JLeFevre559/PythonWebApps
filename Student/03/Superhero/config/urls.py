"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path 
from photos.views import PhotosView
from photos.views import PhotoView
from hero.views import HeroesView, HeroView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('photos/<str:name>', PhotoView.as_view()), 
    path('photos/', PhotosView.as_view()),
    path('', HeroesView.as_view()),
    path('<str:name>', HeroView.as_view()),
]
