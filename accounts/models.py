from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='follower')
    watched_list = models.ManyToManyField(Movie, related_name='watched_list')