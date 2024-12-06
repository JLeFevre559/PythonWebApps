from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Note


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class NoteDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.note1 = dict(user=self.user)
    #     Note.objects.create(**self.note1)

    # def test_add(self):
    #     self.assertEqual(len(Note.objects.all()), 0)
    #     Note.objects.create(**self.note1)
    #     x = Note.objects.get(pk=1)
    #     self.assertEqual(x.title, self.note1['title'])
    #     self.assertEqual(len(Note.objects.all()), 1)
    #
    # def test_edit(self):
    #     Note.objects.create(**self.note1)
    #     x = Note.objects.get(pk=1)
    #     x.title = self.note2['title']
    #     x.body = self.note2['body']
    #     x.save()
    #     self.assertEqual(x.title, self.note2['title'])
    #     self.assertEqual(x.body, self.note2['body'])
    #     self.assertEqual(len(Note.objects.all()), 1)
    #
    # def test_delete(self):
    #     Note.objects.create(**self.note1)
    #     b = Note.objects.get(pk=1)
    #     b.delete()
    #     self.assertEqual(len(Note.objects.all()), 0)


class NoteViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()
        self.note1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.note2 = dict(title='Doc Title 2', body='Doc Body 2')

    # def test_home(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('note_list'))

    # def test_note_list_view(self):
    #     self.assertEqual(reverse('note_list'), '/note/')
    #     Note.objects.create(**self.note1)
    #     Note.objects.create(**self.note2)
    #     response = self.client.get('/note/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'note_list.html')
    #     self.assertTemplateUsed(response, 'theme.html')
    #     self.assertContains(response, '<tr>', count=3)
    #
    # def test_note_detail_view(self):
    #     Note.objects.create(**self.note1)
    #     self.assertEqual(reverse('note_detail', args='1'), '/note/1')
    #     self.assertEqual(reverse('note_detail', args='2'), '/note/2')
    #     response = self.client.get(reverse('note_detail', args='1'))
    #     self.assertContains(response, 'body')
    #
    # def test_note_add_view(self):
    #
    #     # Add without Login
    #     response = self.client.post(reverse('note_add'), self.note1)
    #     response = self.client.post(reverse('note_add'), self.note2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/note/add')
    #
    #     # Login to add
    #     self.login()
    #     response = self.client.post(reverse('note_add'), self.note1)
    #     response = self.client.post(reverse('note_add'), self.note2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     self.assertEqual(len(Note.objects.all()), 2)
    #
    # def test_note_edit_view(self):
    #
    #     # Edit without Login
    #     response = Note.objects.create(**self.note1)
    #     response = self.client.post(reverse('note_edit', args='1'), self.note2)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/accounts/login/?next=/note/1/')
    #
    #     # Login to edit
    #     self.login()
    #     response = self.client.post('/note/1/', self.note2)
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get(response.url)
    #     note = Note.objects.get(pk=1)
    #     self.assertEqual(note.title, self.note2['title'])
    #     self.assertEqual(note.body, self.note2['body'])
    #
    # def test_note_delete_view(self):
    #     self.login()
    #     Note.objects.create(**self.note1)
    #     self.assertEqual(reverse('note_delete', args='1'), '/note/1/delete')
    #     response = self.client.post('/note/1/delete')
    #     self.assertEqual(len(Note.objects.all()), 0)
