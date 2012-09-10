{% if False %}
django_project
==============

My initial django project structure for new projects. Requires Django 1.4

Use the django-admin startproject command to create a new project with this as the template:
django-admin startproject project_name --template=https://github.com/jukvalim/django_project/zipball/master --extension=py,md

Use pip to install dependencies (you're using virtualenv, I hope):
pip install -r requirements.txt

Go to project directory and create development database:
python manage.py syncdb

Now you should be able to run development server with Werkzeug debugger:
python manage.py runserver_plus
{% endif %}
{{ project_name|title }}
==============

Write project description here