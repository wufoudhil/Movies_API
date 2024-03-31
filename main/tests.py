import pytest
import celery 
from django.urls import reverse

from .models import Movie
from tasks import reverse_string  

@pytest.mark.django_db
def test_movie_create():
  m = Movie(name="Movie_Test_Name", protagonists="Movie_Test_protagonists", poster="Movie_Test_poster")
  m.save()
  assert Movie.objects.count() == 1


@pytest.mark.django_db
def test_view(client):
   url = reverse('api/')
   response = client.get(url)
   assert response.status_code == 200


