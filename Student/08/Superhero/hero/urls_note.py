
from django.urls import path

from .views_note import NoteDeleteView, NoteDetailView, NoteListView, NoteCreateView, NoteUpdateView


urlpatterns = [

    # Note
    path('note/',                       NoteListView.as_view(),    name='note_list'),
    path('note/<int:pk>',               NoteDetailView.as_view(),  name='note_detail'),
    path('note/add',                    NoteCreateView.as_view(),  name='note_add'),
    path('note/<int:pk>/',              NoteUpdateView.as_view(),  name='note_edit'),
    path('note/<int:pk>/delete',        NoteDeleteView.as_view(),  name='note_delete'),

]
