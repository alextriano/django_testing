from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from notes.models import Note


User = get_user_model()


class TestRoutes(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Автор')
        cls.reader = User.objects.create(username='Читатель')
        cls.note = Note.objects.create(
            title='Заголовок',
            text='Текст',
            author=cls.author,
        )

    def test_pages_availability(self):
        """Доступность страниц анонимным пользователям."""
        urls = (
            ('notes:home', None),
            ('users:login', None),
            ('users:logout', None),
            ('users:signup', None),
        )
        for name, args in urls:
            with self.subTest(name=name):
                url = reverse(name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_availability_for_note_autorized_user(self):
        """Доступность страниц авторизованным пользователям."""
        users_statuses = (
            (self.reader, HTTPStatus.OK),
        )
        for user, status in users_statuses:
            self.client.force_login(user)
            for name in (
                'notes:list',
                'notes:success',
                'notes:add',
            ):
                with self.subTest(user=user, name=name):
                    url = reverse(name,)
                    response = self.client.get(url)
                    self.assertEqual(response.status_code, status)

    def test_availability_for_note_edit_and_delete(self):
        """Доступность страниц авторам-пользователям."""
        users_statuses = (
            (self.author, HTTPStatus.OK),
            (self.reader, HTTPStatus.NOT_FOUND),
        )
        for user, status in users_statuses:
            self.client.force_login(user)
            for name in (
                'notes:edit',
                'notes:delete',
                'notes:detail',
            ):
                with self.subTest(user=user, name=name):
                    url = reverse(name, args=(self.note.slug,))
                    response = self.client.get(url)
                    self.assertEqual(response.status_code, status)

    def test_redirect_for_anonymous_client(self):
        """Редирект для анонимных пользователей."""
        login_url = reverse('users:login')
        for name in (
            'notes:detail',
            'notes:edit',
            'notes:delete',
        ):
            with self.subTest(name=name):
                url = reverse(name, args=(self.note.slug,))
                redirect_url = f'{login_url}?next={url}'
                response = self.client.get(url)
                self.assertRedirects(response, redirect_url)

        for name in (
            'notes:list',
            'notes:success',
            'notes:add',
        ):
            with self.subTest(name=name):
                url = reverse(name,)
                redirect_url = f'{login_url}?next={url}'
                response = self.client.get(url)
                self.assertRedirects(response, redirect_url)
