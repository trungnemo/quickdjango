from django.db import models

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
