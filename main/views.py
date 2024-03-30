from django.http import HttpResponse
from ninja import NinjaAPI
from .models import Movie



api = NinjaAPI()

@api.get("/MovieList/")
def MovieList(request):
    return {"movies": Movie.objects.all().order_by('ranking').values()}


