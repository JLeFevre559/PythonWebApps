from django.test import TestCase
from .models import Superhero

# Create your tests here.
class SuperheroTestCase(TestCase):
    def test_superhero_model(self):
        superhero = Superhero.objects.create(
            name='Superman',
            identity='Clark Kent',
            description='Superman is a superhero',
            image='superman.jpg',
            strengths='Super strength, flight, invulnerability',
            weaknesses='Kryptonite',
        )
        self.assertEqual(superhero.name, 'Superman')
        self.assertEqual(superhero.identity, 'Clark Kent')
        self.assertEqual(superhero.description, 'Superman is a superhero')
        self.assertEqual(superhero.image, 'superman.jpg')
        self.assertEqual(superhero.strengths, 'Super strength, flight, invulnerability')
        self.assertEqual(superhero.weaknesses, 'Kryptonite')

    def test_superhero_list_view(self):
        response = self.client.get('/hero/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/list.html')

    def test_superhero_detail_view(self):
        superhero = Superhero.objects.create(
            name='Superman',
            identity='Clark Kent',
            description='Superman is a superhero',
            image='superman.jpg',
            strengths='Super strength, flight, invulnerability',
            weaknesses='Kryptonite',
        )
        response = self.client.get(f'/hero/{superhero.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/detail.html')
    
    def test_superhero_create_view(self):
        response = self.client.get('/hero/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/add.html')

    def test_superhero_update_view(self):
        superhero = Superhero.objects.create(
            name='Superman',
            identity='Clark Kent',
            description='Superman is a superhero',
            image='superman.jpg',
            strengths='Super strength, flight, invulnerability',
            weaknesses='Kryptonite',
        )
        response = self.client.get(f'/hero/{superhero.pk}/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/edit.html')
    
    def test_superhero_delete_view(self):
        superhero = Superhero.objects.create(
            name='Superman',
            identity='Clark Kent',
            description='Superman is a superhero',
            image='superman.jpg',
            strengths='Super strength, flight, invulnerability',
            weaknesses='Kryptonite',
        )
        response = self.client.get(f'/hero/{superhero.pk}/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/delete.html')

