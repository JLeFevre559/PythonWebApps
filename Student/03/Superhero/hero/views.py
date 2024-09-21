from django.shortcuts import render
from django.views.generic import TemplateView
from pathlib import Path

class HeroView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        p = kwargs['name']
        
        return dict(hero = heroes_list()[p])

def heroes_list():
    return {
        'iron_man':{
            'name':'Iron Man', 
            'description':"A genius, billionaire, playboy, philanthropist, and superhero.", 
            'identity':"Tony Stark",
            'image':'iron_man',
        },
        'black_widow':{
            'name':'Black Widow', 
            'description':"A former KGB assassin and agent of S.H.I.E.L.D.", 
            'identity':"Natasha Romanoff",
            'image':'black_widow',
        },
        'hulk':{
            'name':'Hulk', 
            'description':"A scientist who transforms into a raging monster when enraged.", 
            'identity':"Bruce Banner",
            'image':'hulk',
            }
        }

class HeroesView(TemplateView):
    template_name = 'heroes.html'
    

    def get_context_data(self, **kwargs):
        ## temporarily hardcoding the hero list
        hero_list = heroes_list()
        return dict(heroes=hero_list)
    
