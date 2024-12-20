from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Superhero, Article, Investigator, Photo
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
import json
import csv

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

def export_heroes(request, file_format):
    superheroes = Superhero.objects.all()

    if file_format == 'json':
        response = HttpResponse(content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="superheroes.json"'

        data = [d for d in superheroes.values()]

        response.write(json.dumps(data, indent=4))
        return response
    
    elif file_format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="superheroes.csv"'

        writer = csv.writer(response)
        writer.writerow(['name', 'identity', 'description', 'image', 'strengths', 'weaknesses'])

        for superhero in superheroes:
            writer.writerow([superhero.name, superhero.identity, superhero.description, superhero.image, superhero.strengths, superhero.weaknesses])

        return response
    
    else:
        return HttpResponse(status=400)
    
def export_articles(request, file_format):
    articles = Article.objects.all()

    if file_format == 'json':
        response = HttpResponse(content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="articles.json"'

        data = [d for d in articles.values()]

        response.write(json.dumps(data, indent=4, default=str))
        return response
    
    elif file_format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="articles.csv"'

        writer = csv.writer(response)
        writer.writerow(['title', 'content', 'author', 'date', 'image', 'hero', 'Investigator'])

        for article in articles:
            writer.writerow([article.title, article.content, article.author, article.date, article.image, article.hero, article.Investigator])

        return response
    
    else:
        return HttpResponse(status=400)
    
class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photo/add.html'
    fields = '__all__'
    success_url = reverse_lazy('photo-list')
    
class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/list.html'
    context_object_name = 'photos'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/detail.html'
    context_object_name = 'photo'

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photo/edit.html'
    fields = '__all__'
    success_url = reverse_lazy('photo-list')

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/delete.html'
    success_url = reverse_lazy('photo-list')

    #on success, this also needs to delete the saved image file
    def delete(self, request, *args, **kwargs):
        photo = self.get_object()
        photo.image.delete()
        return super().delete(request, *args, **kwargs)
    
def photo_data(id, photo):
        x = dict(image_url=f"/media/{photo.image}", 
                 id=str(id), 
                 label=f"Photo {photo.image} {id}")
        if id == 0:
            x.update(active="active", aria='aria-current="true"')
        return x    
def carousel_data(photos):
            return [photo_data(id, photo) for id, photo in enumerate(photos)]

class PhotoCarouselView(TemplateView):
    template_name = 'photo/carousel.html'

    def get_context_data(self, **kwargs):
        photos = Photo.objects.all()
        return dict(title='Carousel View', carousel=carousel_data(photos))


    

    