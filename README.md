# myblog

This is the testing site based on the tutorial of http://www.51bxl.cn/blog/2/

~~~
virtualenv venv
venv\scripts\activate
pip install -r requirements.txt

mysql> create database blog default charset=utf8;
python manage.py  makemigrations
python manage.py migrate
python manage.py createsuperuser


python manage.py runserver
~~~

