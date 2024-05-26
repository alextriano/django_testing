# Django testing  
Тестирование проектов YaNote и YaNews на unittest и pytest соответственно.
Django-проект YaNews: новостной сайт, где пользователи могут оставлять комментарии к новостям.
Django-проект YaNote: электронная записная книжка для тех, кто не хочет ничего забыть и поэтому всё записывает. 

## Разверните проекты на своём компьютере:
На своём компьютере в директории с проектами создайте папку для проекта YaNews.
Склонируйте проект YaNews из репозитория: 
```
git clone https://github.com/alextriano/django_testing.git
```
Создайте виртуальное окружение 
```
python -m venv venv
```
Запустите виртуальное окружение и установите зависимости из файла requirements.txt: 
```
pip install -r requirements.txt
```
Миграции уже созданы, выполните их: 
```
python manage.py migrate.
```
Cоздайте суперпользователя: 
```
python manage.py createsuperuser.
```
Для заполнения базы данных новостями, выполните команду 
```
python manage.py loaddata news.json.
```
Запустите проект:
```
python manage.py runserver
```
