from django.db import models

# Create your models here.

status = [
    ('0', 'coming-up'),
    ('1', 'starting'),
    ('2', 'running'),
    ('3', '')
]
class movie(models.Model):
    name = models.CharField(max_length=200)
    protagonists = models.TextField()
    poster = models.ImageField()
    trailer = models.URLField()
    start_date = models.DateField()
    status = models.CharField(max_length=1, choices=status)
    ranking = models.IntegerField()