## Anotation

This project is a demonstration of acquired skills. It will be updated for next month untill all done.
Main backend configurations are set (urls for each app, views, api for each app, templates, etc) for deploying on working server <br/>

## Enviroment 

#### create virtual enviroment via `virtualenv venv` <br/>
activate enviroment:<br/>
##### `source ./venv/bin/activate` [Linux]<br/>
##### `venv\Scripts\activate` [Windows]<br/>

## Install Requirements

#### `pip install -r requirements.txt`

#### `linux` users:
create  `.env` file in main directory and fill the followings:
	
	SECRET_KEY = "Your Data goes herer"
	DB_NAME = "Your Data goes herer"
	DB_USER = "Your Data goes herer"
	DB_PASSWORD = "Your Data goes herer"
	DB_HOST = "Your Data goes herer"
	DB_PORT = "Your Data goes herer"
	EMAIL_HOST = "Your Data goes herer"
	EMAIL_PORT = "Your Data goes herer"
	EMAIL_HOST_USER = "Your Data goes herer"
	EMAIL_HOST_PASSWORD = "Your Data goes herer"
	EMAIL_USE_TLS = "Your Data goes herer"
	DEFAULT_FROM_EMAIL = "Your Data goes herer"
	REDIS_LOCATION = "Your Data goes herer"
	GS_BUCKET_NAME = "Your Data goes herer"
	GS_PROJECT_ID = "Your Data goes herer"
	GS_MEDIA_BUCKET_NAME = "Your Data goes herer"

#### `Windows` users:
You need to specify all these in enviroment variables (example: [Youtube](https://www.youtube.com/watch?v=bEroNNzqlF4))

## Migration

after you declare all variables and input all needed data in them. run command:
#### `python manage.py migrate`
then you need to create a superuser:
#### `python manage.py createsuperuser`

## Run server

Now you ready to go, open terminal and type command: `python manage.py runserver`. It will run the project in the development mode.<br />
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

## Learn More

You can learn more in the [Django documentation](https://docs.djangoproject.com/en/3.1/).

To learn DRF, check out the [Django Rest Framework documentation](https://www.django-rest-framework.org/).

JSON Web Token Authentication support for Django REST Framework [REST framework JWT Auth](https://jpadilla.github.io/django-rest-framework-jwt/).

Deploy Django application on [Heroku Devcenter](https://devcenter.heroku.com/categories/python-support) 

For hosting static and media files use [Google Cloud Storage](https://cloud.google.com/storage/docs/hosting-static-website)
