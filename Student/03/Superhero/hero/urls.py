from django.urls import path
from .views import BlackWidow, HulkView, IndexView, IronManView

urlpatterns = [
    path('', IndexView.as_view()),
    path('hulk', HulkView.as_view()),
    path('iron_man', IronManView.as_view()),
    path('black_widow', BlackWidow.as_view()),
]
