from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models_note import Note


class NoteView(RedirectView):
    url = reverse_lazy('note_list')


class NoteListView(ListView):
    template_name = 'note/list.html'
    model = Note
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    template_name = 'note/detail.html'
    model = Note
    context_object_name = 'note'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     note = kwargs.get('note')
    #     kwargs['dependents'] = note.dependents
    #     return kwargs


class NoteCreateView(LoginRequiredMixin, CreateView):
    template_name = "note/add.html"
    model = Note
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instance.book = 1
    #     form.instance.author = Person.get_me(self.request.user)
    #     return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "note/edit.html"
    model = Note
    fields = '__all__'


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'note/delete.html'
    success_url = reverse_lazy('note_list')
