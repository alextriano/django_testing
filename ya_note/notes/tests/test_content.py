from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from notes.models import Note


User = get_user_model()


class TestContentPage(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Автор')
        cls.note = Note.objects.create(
            title='Заголовок',
            text='Текст',
            author=cls.author,
        )
        cls.add_url = reverse('notes:add')
        cls.list_url = reverse('notes:list')
        cls.edit_url = reverse('notes:edit', args=(cls.note.slug,))

    def test_note_in_list_for_author(self):
        """Отдельная заметка передаётся на страницу со списком заметок."""
        self.client.force_login(self.author)
        response = self.client.get(self.list_url)
        object_list = response.context['object_list']
        self.assertIn(self.note, object_list)

    def test_note_not_in_list_for_another_user(self):
        """В списке заметок одного пользователя нет заметок другого."""
        self.client.force_login(self.author)
        response = self.client.get(self.list_url)
        object_list = response.context['object_list']
        self.assertNotIn('note', object_list)

    def test_add_page_have_form(self):
        """На страницу создания заметки передается форма."""
        self.client.force_login(self.author)
        response = self.client.get(self.add_url)
        self.assertIn('form', response.context)

    def test_edit_page_have_form(self):
        """На страницу редактирования заметки передается форма."""
        self.client.force_login(self.author)
        response = self.client.get(self.edit_url)
        self.assertIn('form', response.context)
