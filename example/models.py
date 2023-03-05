from django.db import models
from django.contrib.auth.models import AbstractUser

categories = [
	('DEVEVELOPPEMENT_PERSONNEL', 'développement personnel'),
	('PHILOSOPHIE', 'philosophie'),
	('FINANCE', 'finance'),
	('BUISNESS', 'buisness'),
]

class Book(models.Model):
    thumbnail = models.URLField(null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.CharField(max_length=50, choices=categories)
    author = models.CharField(max_length=50)
    duration = models.DurationField()
    amazon_link = models.URLField()
    youtube_link = models.URLField()
    notes = models.TextField()
    ebook_link = models.URLField(null=True)
    date_upload = models.CharField(max_length=300, null=True)
    my_review = models.TextField(null=True)

class Shopper(AbstractUser):
    pass


class Comment(models.Model):
    user = models.ForeignKey(Shopper, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)