import pytest

from news.models import News, Comment


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
def author_client(author, client):
    client.force_login(author)
    return client


@pytest.fixture
def news():
    news = News.objects.create(
        title='Заголовок',
        text='Текст',
    )
    return news


@pytest.fixture
def comment(author, news):
    comment = Comment.objects.create(
        news=news,
        text='Комментарий',
        author=author
    )
    return comment


@pytest.fixture
def id_for_args(comment):
    return comment.id,


@pytest.fixture
def form_data():
    return {'text': 'Новый текст'}
