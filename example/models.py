from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


"""
categories = [
	('DEVEVELOPPEMENT_PERSONNEL', 'développement personnel'),
	('PHILOSOPHIE', 'philosophie'),
	('FINANCE', 'finance'),
	('BUISNESS', 'buisness'),
]

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    thumbnail = models.ImageField(upload_to='book_thumbnails')
    title = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.CharField(max_length=50, choices=categories)
    author = models.CharField(max_length=50)
    duration = models.DurationField()
    amazon_link = models.URLField()
    youtube_link = models.URLField()
    notes = models.TextField()
"""




