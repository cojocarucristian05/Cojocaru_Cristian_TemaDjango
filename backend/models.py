from django.db import models

# Create your models here.
from django.utils import timezone


class Article(models.Model):
    title   = models.CharField(max_length = 120)
    content = models.TextField()
    date    = models.DateField(auto_now_add = True )


    def __str__(self):
        return self.title
