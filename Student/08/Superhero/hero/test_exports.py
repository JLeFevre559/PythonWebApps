from .models import Superhero, Article
from django.test import TestCase
from django.urls import reverse
from .views import export_heroes
import json
from django.contrib.auth.models import User

class test_exports(TestCase):
    def setUp(self):
        # create account
        self.client.post('/accounts/signup/', {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        # login
        self.client.post('/accounts/login/', {'username': 'testuser', 'password': 'testpassword'})
        # create superhero
        superhero = Superhero.objects.create(
            name='Superman',
            identity='Clark Kent',
            description='Superman is a superhero',
            image='superman.jpg',
            strengths='Super strength, flight, invulnerability',
            weaknesses='Kryptonite',
        )
        self.user = User.objects.get(username='testuser')
        article = Article.objects.create(
            title='Superman Saves the Day',
            content='Superman saved the day by stopping a bank robbery',
            author=self.user.username,
            date='2021-01-01',
            image='superman-saves-the-day.jpg',
            hero=superhero,
        )
        

    def test_export_heroes(self):
        response = self.client.get(reverse('export_heroes', args=['json']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="superheroes.json"')
        self.assertEqual(json.loads(response.content), [{'description': 'Superman is a superhero',
                                                                'id': 1,
                                                                'identity': 'Clark Kent',
                                                                'image': 'superman.jpg',
                                                                'name': 'Superman',
                                                                'strengths': 'Super strength, flight, invulnerability',
                                                                'weaknesses': 'Kryptonite'}])

        response = self.client.get(reverse('export_heroes', args=['csv']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="superheroes.csv"')
        self.assertEqual(response.content, b'name,identity,description,image,strengths,weaknesses\r\nSuperman,Clark Kent,Superman is a superhero,superman.jpg,"Super strength, flight, invulnerability",Kryptonite\r\n')

    def test_export_articles(self):
        response = self.client.get(reverse('export_articles', args=['json']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="articles.json"')
        self.assertEqual(json.loads(response.content), [{'author': 'testuser',
                                                                'content': 'Superman saved the day by stopping a bank robbery',
                                                                'date': '2021-01-01',
                                                                'hero_id': 1,
                                                                'id': 1,
                                                                'image': 'superman-saves-the-day.jpg',
                                                                'Investigator_id': None,
                                                                'title': 'Superman Saves the Day'}])

        response = self.client.get(reverse('export_articles', args=['csv']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="articles.csv"')
        self.assertEqual(response.content, b'title,content,author,date,image,hero,Investigator\r\nSuperman Saves the Day,Superman saved the day by stopping a bank robbery,testuser,2021-01-01,superman-saves-the-day.jpg,Superman,\r\n')

