from django.shortcuts import render
from .models import Superhero
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import TemplateView

class homeView(TemplateView):
    template_name = 'index.html'
    
class HeroListView(ListView):
     model = Superhero
     template_name = 'hero/list.html'
     context_object_name = 'superheroes'

class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'hero/detail.html'
    context_object_name = 'superhero'

class HeroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'hero/add.html'
    fields = '__all__'
    success_url = reverse_lazy('hero-list')

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'hero/edit.html'
    fields = '__all__'
    success_url = reverse_lazy('hero-list')

class HeroDeleteView(DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero-list')

class SignUpView(View):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect(reverse_lazy('hero-list'))  # Replace 'home' with your actual URL name

        return render(request, self.template_name, {'form': form})