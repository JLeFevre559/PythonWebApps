from django.shortcuts import render
from django.views.generic import TemplateView
from pathlib import Path
from .models import Superhero

class HeroView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        p = kwargs['name']
        h= Superhero.objects.get(image=p)
        return dict(hero = h)


class HeroesView(TemplateView):
    template_name = 'heroes.html'
    

    def get_context_data(self, **kwargs):
        hero_list = Superhero.objects.all()
        return dict(heroes=hero_list)
    
