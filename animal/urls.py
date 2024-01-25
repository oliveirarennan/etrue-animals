from django.urls import path
from .views import home, CreateSpecieView, CreateAnimalView

urlpatterns = [
  path('', home, name='home'),
  path('create_specie/', CreateSpecieView, name='create_specie'),
  path('create_animal/', CreateAnimalView, name='create_animal'),
]