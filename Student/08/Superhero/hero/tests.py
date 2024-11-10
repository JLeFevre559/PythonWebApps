from django.test import TestCase
from .models import Superhero, Article, Investigator
from django.contrib.auth.models import User

# Create your tests here.
class SuperheroTestCase(TestCase):
    def setUp(self):
        # create account
        self.client.post('/accounts/signup/', {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        # login
        self.client.post('/accounts/login/', {'username': 'testuser', 'password': 'testpassword'})


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

class ArticleTestCase(TestCase):
    def setUp(self):
        # create account
        self.client.post('/accounts/signup/', {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        # login
        self.client.post('/accounts/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.user = User.objects.get(username='testuser')

    def test_article_model(self):
        superhero = Superhero.objects.create(
            name='Superman',
            identity='Clark Kent',
            description='Superman is a superhero',
            image='superman.jpg',
            strengths='Super strength, flight, invulnerability',
            weaknesses='Kryptonite',
        )
        article = Article.objects.create(
            title='Superman Saves the Day',
            content='Superman saved the day by stopping a bank robbery',
            author=self.user.username,
            date='2021-01-01',
            image='superman-saves-the-day.jpg',
            hero=superhero,
        )
        self.assertEqual(article.title, 'Superman Saves the Day')
        self.assertEqual(article.content, 'Superman saved the day by stopping a bank robbery')
        self.assertEqual(article.author, self.user.username)
        self.assertEqual(article.date, '2021-01-01')
        self.assertEqual(article.image, 'superman-saves-the-day.jpg')
        self.assertEqual(article.hero, superhero)
    
    def test_article_list_view(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/list.html')

    def test_article_detail_view(self):
        superhero = Superhero.objects.create(
            name='Superman',
            identity='Clark Kent',
            description='Superman is a superhero',
            image='superman.jpg',
            strengths='Super strength, flight, invulnerability',
            weaknesses='Kryptonite',
        )
        article = Article.objects.create(
            title='Superman Saves the Day',
            content='Superman saved the day by stopping a bank robbery',
            author='Lois Lane',
            date='2021-01-01',
            image='superman-saves-the-day.jpg',
            hero=superhero,
        )
        response = self.client.get(f'/articles/{article.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/detail.html')
    
    def test_article_create_view(self):
        response = self.client.get('/articles/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/add.html')

    def test_article_update_view(self):
        superhero = Superhero.objects.create(
            name='Superman',
            identity='Clark Kent',
            description='Superman is a superhero',
            image='superman.jpg',
            strengths='Super strength, flight, invulnerability',
            weaknesses='Kryptonite',
        )
        article = Article.objects.create(
            title='Superman Saves the Day',
            content='Superman saved the day by stopping a bank robbery',
            author=self.user.username,
            date='2021-01-01',
            image='superman-saves-the-day.jpg',
            hero=superhero,
        )
        response = self.client.get(f'/articles/{article.pk}/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/edit.html')

        # test that only the author can update the article
        self.client.post('/accounts/logout/')
        self.client.post('/accounts/signup/', {'username': 'testuser1', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.client.post('/accounts/login/', {'username': 'testuser1', 'password': 'testpassword'})
        user = User.objects.get(username='testuser')
        response = self.client.get(f'/articles/{article.pk}/edit/')
        self.assertEqual(response.status_code, 403)

    def test_article_delete_view(self):
        superhero = Superhero.objects.create(
            name='Superman',
            identity='Clark Kent',
            description='Superman is a superhero',
            image='superman.jpg',
            strengths='Super strength, flight, invulnerability',
            weaknesses='Kryptonite',
        )
        article = Article.objects.create(
            title='Superman Saves the Day',
            content='Superman saved the day by stopping a bank robbery',
            author=self.user.username,
            date='2021-01-01',
            image='superman-saves-the-day.jpg',
            hero=superhero,
        )
        response = self.client.get(f'/articles/{article.pk}/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/delete.html')

        # test that only the author can delete the article
        self.client.post('/accounts/logout/')
        self.client.post('/accounts/signup/', {'username': 'testuser1', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.client.post('/accounts/login/', {'username': 'testuser1', 'password': 'testpassword'})
        user = User.objects.get(username='testuser')
        response = self.client.get(f'/articles/{article.pk}/delete/')
        self.assertEqual(response.status_code, 403)
        
class InvestigatorTestCase(TestCase):
    def setUp(self):
        # create account
        self.client.post('/accounts/signup/', {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        # login
        self.client.post('/accounts/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.user = User.objects.get(username='testuser')

    def test_investigator_model(self):
        investigator = Investigator.objects.create(
            user=self.user,
            name='Sherlock Holmes',
        )
        self.assertEqual(investigator.user, self.user)
        self.assertEqual(investigator.name, 'Sherlock Holmes')

    def test_investigator_create_view(self):
        response = self.client.get('/investigator/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'investigator/add.html')

    def test_investigator_update_view(self):
        investigator = Investigator.objects.create(
            user=self.user,
            name='Sherlock Holmes',
        )
        response = self.client.get(f'/investigator/{investigator.pk}/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'investigator/edit.html')
    
    def test_investigator_delete_view(self):
        investigator = Investigator.objects.create(
            user=self.user,
            name='Sherlock Holmes',
        )
        response = self.client.get(f'/investigator/{investigator.pk}/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'investigator/delete.html')

        # test that only logged in users can delete the investigator
        self.client.post('/accounts/logout/')
        response = self.client.get(f'/investigator/{investigator.pk}/delete/')
        self.assertEqual(response.status_code, 302)

    def test_investigator_list_view(self):
        response = self.client.get('/investigator/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'investigator/list.html')

    def test_investigator_detail_view(self):
        investigator = Investigator.objects.create(
            user=self.user,
            name='Sherlock Holmes',
        )
        response = self.client.get(f'/investigator/{investigator.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'investigator/detail.html')
