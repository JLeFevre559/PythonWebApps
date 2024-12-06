
from django.urls import path

from .views_testy import testboiDeleteView, testboiDetailView, testboiListView, testboiCreateView, testboiUpdateView


urlpatterns = [

    # testboi
    path('testy/',                       testboiListView.as_view(),    name='testy_list'),
    path('testy/<int:pk>',               testboiDetailView.as_view(),  name='testy_detail'),
    path('testy/add',                    testboiCreateView.as_view(),  name='testy_add'),
    path('testy/<int:pk>/',              testboiUpdateView.as_view(),  name='testy_edit'),
    path('testy/<int:pk>/delete',        testboiDeleteView.as_view(),  name='testy_delete'),

]
