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
## Add a Bootstrap 4 to the project
- What boottrap is
- How to use it int our project
```html
<!--Goto the https://getbootstrap.com/docs/5.1/getting-started/introduction/-->
<html>
   <title>
      <!-- Bootstrap CSS -->
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-  KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
   </title>
   <body>
        <!-- Option 2: Separate Popper and Bootstrap JS -->
       <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp" crossorigin="anonymous"></script>
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
      
        <!---Goto Component Get the navbar and copy in here->

   </body>
</html>
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
I use this to teach my son
## License
[MIT](https://choosealicense.com/licenses/mit/)
