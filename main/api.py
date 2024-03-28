from typing import List
from ninja import NinjaAPI, ModelSchema
from .models import Movie

api = NinjaAPI()

class MoviSchema(ModelSchema):
    class Config:
        model = Movie
        model_fields = ['name', 'protagonists', 'poster', 'trailer', 'start_date', 'status', 'ranking']

@api.get("/MovieList/", response=List[MoviSchema])
def MovieList(request):
    return Movie.objects.all().order_by('-ranking')