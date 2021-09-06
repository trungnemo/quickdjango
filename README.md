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
Create a django project
```bash
django-admin createproject quickdjango
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
from movieapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
# Add a .\templates\home.html
```
## Django Admin Dashboard
```bash
# ini the db structure for the dashboard
python manage.py migrate
# create a super user
# my 'template'
python manage.py createsuperuser
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
I use this to teach my son
## License
[MIT](https://choosealicense.com/licenses/mit/)
