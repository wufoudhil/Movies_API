# Generated by Django 4.2.5 on 2024-03-28 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_movie_name_alter_movie_poster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.IntegerField(choices=[(0, 'coming-up'), (1, 'starting'), (2, 'running'), (3, 'finished')]),
        ),
    ]