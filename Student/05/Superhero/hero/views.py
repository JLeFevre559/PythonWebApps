from django.shortcuts import render
from .models import Superhero
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class HeroListView(ListView):
     model = Superhero
     template_name = 'hero/list.html'
     context_object_name = 'superheroes'

class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'hero/detail.html'
    context_object_name = 'superhero'

class HeroCreateView(CreateView):
    model = Superhero
    template_name = 'hero/add.html'
    fields = '__all__'
    success_url = reverse_lazy('hero-list')

class HeroUpdateView(UpdateView):
    model = Superhero
    template_name = 'hero/edit.html'
    fields = '__all__'
    success_url = reverse_lazy('hero-list')

class HeroDeleteView(DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero-list')