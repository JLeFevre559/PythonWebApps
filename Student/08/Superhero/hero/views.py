from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Superhero, Article, Investigator
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied
from .forms import ArticleForm, InvestigatorForm
import markdown

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
    
class ArticleListView(ListView):
    model = Article
    template_name = 'article/list.html'
    context_object_name = 'articles'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article/add.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article-list')


    def form_valid(self, form):
        # Set the author field to the current user's username before saving
        form.instance.author = self.request.user.username
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'

#Article Update View requires username of logged in user to match author of article
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article/edit.html'
    success_url = reverse_lazy('article-list')
    form_class = ArticleForm

    def get_object(self, queryset=None):
        article = super().get_object(queryset)

        # Check if the current user is the author of the object
        if article.author != self.request.user.username:
            raise PermissionDenied("You do not have permission to delete this object.")

        return article
    
#Article Delete View requires username of logged in user to match author of article
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article/delete.html'
    success_url = reverse_lazy('article-list')

    def get_object(self, queryset=None):
        article = super().get_object(queryset)

        # Check if the current user is the author of the object
        if article.author != self.request.user.username:
            raise PermissionDenied("You do not have permission to delete this object.")

        return article
    
class PageView(TemplateView):

    def get_template_names(self):
        page = self.kwargs.get('page', 'index')
        return f'{page}.html'
    
class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = "Documents/" + self.kwargs.get('doc', 'document') + ".md"
        print(document)
        markdown_text = open(document).read()
        print(markdown_text)
        return dict(html= markdown.markdown(markdown_text))
    
class InvestigatorCreateView(LoginRequiredMixin, CreateView):
    model = Investigator
    template_name = 'investigator/add.html'
    form_class = InvestigatorForm
    success_url = reverse_lazy('investigator-list')


class InvestigatorListView(ListView):
    model = Investigator
    template_name = 'investigator/list.html'
    context_object_name = 'investigators'

class InvestigatorDetailView(DetailView):
    model = Investigator
    template_name = 'investigator/detail.html'
    context_object_name = 'investigator'

class InvestigatorUpdateView(LoginRequiredMixin, UpdateView):
    model = Investigator
    template_name = 'investigator/edit.html'
    form_class = InvestigatorForm
    success_url = reverse_lazy('investigator-list')

class InvestigatorDeleteView(LoginRequiredMixin, DeleteView):
    model = Investigator
    template_name = 'investigator/delete.html'
    success_url = reverse_lazy('investigator-list')
    