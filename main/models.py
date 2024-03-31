from django.db import models

# Create your models here.

status = [
    ('coming-up', 'coming-up'),
    ('starting', 'starting'),
    ('running', 'running'),
    ('finished', 'finished')
]

class Movie(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default='')
    protagonists = models.TextField(null=True, blank=True, default='')
    poster = models.ImageField(null=True, blank=True)
    trailer = models.URLField(null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=status)
    ranking = models.IntegerField()


    def __str__(self):
        return self.name
