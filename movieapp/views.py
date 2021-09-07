from django.shortcuts import render
from .models import Movie
# home page
def home(request):
    #Simple test to pass the data fromt the model to the html template
    #movie_data = "John Wick"

    # movie_data = [
    #     {
    #         "name": "Microsoft Python Tutorial",
    #         "year": "2019"
    #     },
    #     {
    #         "name": "John Wich Chapter 4",
    #         "year": "2021"
    #     },
    #     {
    #         "name": "Iron Mask",
    #         "year": "2020"
    #     },
    # ]

    #List all the movie records fromt he movie table in the database
    #movie_data = Movie.objects.all() 
    
    #Filter the movie records fromt he movie table in the database
    #That has star > 2 AND year >= 2015
    movie_data = Movie.objects.filter(star__gt=2, year__gt=2015)
    
    return render(request, 'home.html',{"movie": movie_data})
# testimonials page
def testimonials(request):
    return render(request, 'testimonials.html',{})

# movie detail view
def movie(request, movie_id):
    movie_data = Movie.objects.get(id = movie_id)
    return render(request, 'movie.html', {"movie": movie_data})