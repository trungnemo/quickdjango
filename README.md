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
## Add a testimonials.html to the movieapp
```python
# add a function in a view
def testimonials(request):
    return render(request, 'testimonials.html',{})
#add the new path to urls.py the project quickdjango
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('testimonials', views.testmonials),
]
```
then create a testimonials.html
goto the https://getbootstrap.com/docs/5.1/layout/columns/
```html
<!-- Copy all from home html into the new page -->
<html>
   <title>Testimonials</title>
   <body>
      <!-- This is copy 3 column layout form bootstrap-->
      <div class="container">
        <h3 class = "mt-5 text-center">Testimonials</h3>
        <div class="row">
          <div class="col order-last">
            Testimonial 1
          </div>
          <div class="col">
            Testimonial 2
          </div>
          <div class="col order-first">
            Testimonial 3
          </div>
        </div>
      </div>
   </body>
</html>
```
## Html template to reuse the navigation bar in the other pages
- Edit the html for navbar with the structure like that 
Online movie  Home Testimonials                                                     User Avartar - User Name[...Profiles, Settings, Logout]
- Use the pravatar.cc to get the random avatars or uifaces.co
- Set the name for the urls.py to use in the href of the navigation bar and others
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('testimonials', views.testimonials, name = 'testimonials'),
]
```
```html
<a class="nav-link" href="{% url 'testimonials' %}">Testimonials</a>
<img src ="https://i.pravatar.cc/300" alt= "Trung Van"></img>
```
- Make Django Template to resue the codes
Create the layout.html in the tempaltes folder of the movieapp
Copy all the content from home.html into it
Replace title with
```html
 {% block title %} {% endblock %}
```
Replcae the content in the body with
```html
 {% block content %} {% endblock %}
```
Then apply it for the layout for the other pages with the structrue 
```html
 {% extends 'layout.html' %}
<!--Title-->
 {% block content %} <title>Page Title</title>{% endblock %}
<!--Content-->
 {% block content %} <h3>Page content</h3> {% endblock %}
```
## Movie Data Model
We will add a Movie model in the models.py of the movieapp 
```pythonfrom django.db import models
# movie model
class Movie(models.Model):
    name = models.CharField(max_length = 200, null = False)
    description = models.TextField(null = False)
    trailer = models.CharField(max_length = 200, null = False)
    year = models.IntegerField(null = False)
    star = models.IntegerField(null = True)
    show = models.BooleanField(default = True)#If no input from User then the default value is True to this property
    
    def __str__(self):
        return self.name
```
- make the migration script to migrate the movie the db
```bash
python manage.py makemigrattions
```
- run the migration script to mighrate the Movie model the db
```bash
python manage.py migrate
```
- register the Movie model to be managed in the Django admin dashboard
```python
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Movie)
```
voila, run the web server and goto the http://127.0.0.1:8080:/admin
-Let's make some improvement for the movie admin dashboad
```python
#Let make some improvement 
class MyMovie(admin.ModelAdmin):
    list_display = ('name','year','star','description')
    list_filter = ('star','show')

admin.site.register(Movie, MyMovie)
```
voila, run the web server for the improvement and goto the http://127.0.0.1:8080:/admin
## Make the test to pass the movie data fromt the home view to home.html
Prepare the test data as an array of dictionary then pass it from view to html
```python
#Demo test data to pass the data from view.py to html 
# home page
def home(request):
    #Simple test to pass the data fromt the model to the html template
    #movie_data = "John Wick"
    movie_data = [
        {
            "name": "Microsoft Python Tutorial",
            "year": "2019"
        },
        {
            "name": "John Wich Chapter 4",
            "year": "2021"
        },
        {
            "name": "Iron Mask",
            "year": "2020"
        },
    ]
    return render(request, 'home.html',{"movie": movie_data})
```
Pass the data from view to home.html
```html
{% extends 'layout.html' %}
<!--Title-->
{% block title %}
<title>Django Demo App</title>
{% endblock %}

<div class="container">
  <!--Content-->
  {% block content %}
  <h1 class="mt-5 text-center">Online Move App</h1>
  <!--<p>{{ movie }}</p>-->
  {% for m in movie %}
  <p>{{ m.name }} - {{m.year}}</p>
  {% endfor %} {% endblock %}
</div>
```
## Pass the movies from the Database to the web pages
- List all the movies
- View a movie details and watch the video
```python
from django.shortcuts import render
from .models import Movie
# home page
def home(request):
    #List all the movie records fromt he movie table in the database
    #movie_data = Movie.objects.all() 
    
    #Filter the movie records fromt he movie table in the database
    #That has star > 2 AND year >= 2015
    movie_data = Movie.object.filter(star__gt=2, year__gt=2015)
    
    return render(request, 'home.html',{"movie": movie_data})
```
Render the list in the home.html
```html
<!-- Copy the code for the bootstrap card at https://getbootstrap.com/docs/5.1/components/card/ -->
{% extends 'layout.html' %}
<!--Title-->
{% block title %}
<title>Django Demo App</title>
{% endblock %}

<div class="container">
  <!--Content-->
  {% block content %}
  <h1 class="mt-5 text-center">Online Move App</h1>
  <!--<p>{{ movie }}</p>-->
  <div class="row mt-5">
    {% for m in movie %}
    <div class="col-sm">
      <div class="card" style="width: 18rem">
        <img
          src="http://img.youtube.com/vi/{{m.trailer}}/maxresdefault.jpg"
          class="card-img-top"
        />
        <div class="card-body">
          <h5 class="card-title">{{ m.name }}e</h5>
          {% if m.star > 4 %}
          <button type="button" class="btn btn-danger">{{ m.star }}</button>
          {% else %}
          <button type="button" class="btn btn-warning">{{ m.star }}</button>
          {% endif %}
          <p class="card-text">{{ m.description }}</p>
          <a href="#" class="btn btn-primary">Trailer</a>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
  {% endblock %}
</div>
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
I use this to teach my son
## License
[MIT](https://choosealicense.com/licenses/mit/)
