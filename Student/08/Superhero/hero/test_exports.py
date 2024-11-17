from .models import Superhero, Article
from django.test import TestCase
from django.urls import reverse
from .views import export_heroes
import json

class test_exports(TestCase):
    def setUp(self):
        # create account
        self.client.post('/accounts/signup/', {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        # login
        self.client.post('/accounts/login/', {'username': 'testuser', 'password': 'testpassword'})
        # create superhero
        Superhero.objects.create(
            name='Superman',
            identity='Clark Kent',
            description='Superman is a superhero',
            image='superman.jpg',
            strengths='Super strength, flight, invulnerability',
            weaknesses='Kryptonite',
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

