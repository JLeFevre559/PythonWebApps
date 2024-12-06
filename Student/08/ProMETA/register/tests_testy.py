from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import testboi


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class testboiDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.testy1 = dict(user=self.user)
    #     testboi.objects.create(**self.testy1)

    # def test_add(self):
    #     self.assertEqual(len(testboi.objects.all()), 0)
    #     testboi.objects.create(**self.testy1)
    #     x = testboi.objects.get(pk=1)
    #     self.assertEqual(x.title, self.testy1['title'])
    #     self.assertEqual(len(testboi.objects.all()), 1)
    #
    # def test_edit(self):
    #     testboi.objects.create(**self.testy1)
    #     x = testboi.objects.get(pk=1)
    #     x.title = self.testy2['title']
    #     x.body = self.testy2['body']
    #     x.save()
    #     self.assertEqual(x.title, self.testy2['title'])
    #     self.assertEqual(x.body, self.testy2['body'])
    #     self.assertEqual(len(testboi.objects.all()), 1)
    #
    # def test_delete(self):
    #     testboi.objects.create(**self.testy1)
    #     b = testboi.objects.get(pk=1)
    #     b.delete()
    #     self.assertEqual(len(testboi.objects.all()), 0)


class testboiViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.testy1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.testy2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('testy_list'))

    # def test_testy_list_view(self):
    #     self.assertEqual(reverse('testy_list'), '/testy/')
    #     testboi.objects.create(**self.testy1)
    #     testboi.objects.create(**self.testy2)
    #     response = self.client.get('/testy/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'testy_list.html')
    #     self.assertTemplateUsed(response, 'theme.html')
    #     self.assertContains(response, '<tr>', count=3)
    #
    # def test_testy_detail_view(self):
    #     testboi.objects.create(**self.testy1)
    #     self.assertEqual(reverse('testy_detail', args='1'), '/testy/1')
    #     self.assertEqual(reverse('testy_detail', args='2'), '/testy/2')
    #     response = self.client.get(reverse('testy_detail', args='1'))
    #     self.assertContains(response, 'body')
    #
    # def test_testy_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('testy_add'), self.testy1)
    #     response = self.client.post(reverse('testy_add'), self.testy2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/testy/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('testy_add'), self.testy1)
    #     response = self.client.post(reverse('testy_add'), self.testy2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(testboi.objects.all()), 2)
    #
    # def test_testy_edit_view(self):
    #
    #     # Edit without Login
    #     response = testboi.objects.create(**self.testy1)
    #     response = self.client.post(reverse('testy_edit', args='1'), self.testy2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/testy/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/testy/1/', self.testy2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     testy = testboi.objects.get(pk=1)
    #     self.assertEqual(testy.title, self.testy2['title'])
    #     self.assertEqual(testy.body, self.testy2['body'])
    #
    # def test_testy_delete_view(self):
    #     self.login()
    #     testboi.objects.create(**self.testy1)
    #     self.assertEqual(reverse('testy_delete', args='1'), '/testy/1/delete')
    #     response = self.client.post('/testy/1/delete')
    #     self.assertEqual(len(testboi.objects.all()), 0)
