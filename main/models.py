from django.db import models

# Create your models here.

status = [
    ('0', 'coming-up'),
    ('1', 'starting'),
    ('2', 'running'),
    ('3', 'finished')
]
class Movie(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default='')
    protagonists = models.TextField(null=True, blank=True, default='')
    poster = models.ImageField(null=True, blank=True)
    trailer = models.URLField(null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=status)
    ranking = models.IntegerField()

    def __str__(self):
        return '{}({})'.format(self.name, self.protagonists)
