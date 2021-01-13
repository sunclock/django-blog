# django_blog
django tutorial by @CoreyMSchafer


# How to run django_blog on local environment
1. Download django_blog directory
~~~
$ git clone https://github.com/sunclock/django_blog.git .
~~~

2. Create virtual environment
~~~
$ pip install -U pip
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
~~~

3. Create Database
~~~
$ python manage.py makemigrations
$ python manage.py migrate
~~~

4. Run server
~~~
$ python manage.py runserver
~~~

5. Access to the django_blog website

default server address is http://127.0.0.1:8000/

---

Tasks
- deploy django-blog using aws/nginx/uwsgi
source: https://nachwon.github.io/django-deploy-1-aws/
