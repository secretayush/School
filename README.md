
```
Then you navigate to the base directory of the project and install the requirements in your virtual environment

```bash
> cd easy-school/easy-school
> pip install -r requirements.txt
```
And finally you make migrations to the database, create a super user, and run the server
```bash
> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
> python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. Alternatively you
can use foreman and gunicorn to run the server locally

```bash
> foreman start
```



