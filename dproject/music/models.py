# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=1000)
class Song(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    file_name=models.CharField(max_length=10)
    son_title=models.CharField(max_length=250)



