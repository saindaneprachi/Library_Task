from django.db import models
from django.contrib.auth.models import User


#book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    unique_code = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    

    def __str__(self):
        return f'{self.title} by {self.author}'
