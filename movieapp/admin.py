from django.contrib import admin
from .models import *
# Register your models here.
#Simple display in dashboard
#admin.site.register(Movie)

#Let make some improvement 
class MyMovie(admin.ModelAdmin):
    list_display = ('name','year','star','description')
    list_filter = ('star','show')

admin.site.register(Movie, MyMovie)