# Quick django

Learn to build an online movie web app with a Django Web Framework in python
- django 3.1.3
- bootstrap 4

## Getting Started

Create a Virtual environment/venv for a movie app
- understand what venv is, why we need it
- how to creat a venv
- install django in the venv

```bash
#command to create a virtual environment for the project folder: venv_quickdjango
python3 -m venv venv_quickdjango
#activate the virutal environment
(venv_quickdjango) .\Scripts\activate
#install django
pip install django==3.1.3
```
Create a movieapp
```python
# Create a movieapp, create a new folder movieapp , in the folderproject quịcdjango
python manage.py startapp movieapp
# Create a Welcome movie app, home page
# add a def home in a view.py
def home(request):
   return render(request, 'home.html', {})
# add home in the project setting urls.py
from django.contrib import admin
from django.urls import path
from movieapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.home),
]
# Add a .\templates\home.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Welcome to Django</title>
  </head>
  <body>
    <h1>Welcome to Django: an Online Movie App</h1>
    <h2>This cource for Thanh Tao</h2>
  </body>
</html>
```
## Django Admin Dashboard
```python
import django....

# my 'template'
foobar.pluralize('word')
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
I use this to teach my son
## License
[MIT](https://choosealicense.com/licenses/mit/)
