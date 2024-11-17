from .models import Superhero, Article, Investigator
import json, csv
from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
from .import_files import import_heroes, import_articles

class test_imports(TestCase):
    def test_import_heroes(self):
        # create a json file
        file = open('heroes.json', 'w')
        file.write('[{"name": "Batman", "identity": "Bruce Wayne", "description": "Batman is a superhero", "image": "batman.jpg", "strengths": "Intelligence, martial arts, gadgets", "weaknesses": "None"}]')
        file.close()
        file = open('heroes.json', 'r')
        response = import_heroes(file, 'json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Superhero.objects.get(name='Batman').identity, 'Bruce Wayne')

        # create a csv file
        file = open('heroes.csv', 'w')
        file.write('name,identity,description,image,strengths,weaknesses\nBatman,Bruce Wayne,Batman is a superhero,batman.jpg,"Intelligence, martial arts, gadgets",None')
        file.close()
        file = open('heroes.csv', 'r')
        response = import_heroes(file, 'csv')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Superhero.objects.get(name='Batman').identity, 'Bruce Wayne')

        
    def test_import_articles(self):
        # create a json file
        file = open('articles.json', 'w')
        file.write('[{"title": "Batman Saves the Day", "content": "Batman saved the day by stopping a bank robbery", "author": "testuser", "date": "2021-01-01", "image": "batman-saves-the-day.jpg", "hero": "Batman", "investigator": null}]')
        file.close()
        Superhero.objects.create(name='Batman', identity='Bruce Wayne', description='Batman is a superhero', image='batman.jpg', strengths='Intelligence, martial arts, gadgets', weaknesses='None')
        file = open('articles.json', 'r')
        response = import_articles(file, 'json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Article.objects.get(title='Batman Saves the Day').author, 'testuser')

        Article.objects.get(title='Batman Saves the Day').delete()

        # create a csv file
        file = open('articles.csv', 'w')
        file.write('title,content,author,date,image,hero,investigator\nBatman Saves the Day,Batman saved the day by stopping a bank robbery,testuser,2021-01-01,batman-saves-the-day.jpg,Batman,')
        file.close()
        file = open('articles.csv', 'r')
        response = import_articles(file, 'csv')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Article.objects.get(title='Batman Saves the Day').author, 'testuser')

        Article.objects.get(title='Batman Saves the Day').delete()
        Superhero.objects.get(name='Batman').delete()