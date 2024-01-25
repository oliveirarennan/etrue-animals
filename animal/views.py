from django.shortcuts import render, redirect
from .forms import CreateSpecieForm, CreateAnimalForm
from .models import Species, Animal
from django.contrib import messages
# Create your views here.

def home(request):
  animals = Animal.objects.all()
  return render(request, 'home.html', {'animals': animals})

def CreateSpecieView(request):
  if request.method == 'POST':
    specie_form = CreateSpecieForm(request.POST)

    if specie_form.is_valid():

      try:
        Species.objects.get(name=specie_form.cleaned_data['name'])
        messages.success(request, 'Error! Espécie existente')
      except:
        specie_form.save()
        
      
      
      return redirect('create_specie')

  else: 
    specie_form = CreateSpecieForm()

  species = Species.objects.all()
  return render(request, 'create_specie.html', {'species': species,'specie_form': specie_form})

def CreateAnimalView(request):
  if request.method == 'POST':
    animal_form = CreateAnimalForm(request.POST)

    if animal_form.is_valid():

      try:
        Animal.objects.get(name=animal_form.cleaned_data['name'])
        messages.success(request, 'Error! Animal já existente')
      except:
        animal_form.save()
        
      
      
      return redirect('create_animal')

  else: 
    animal_form = CreateAnimalForm()

  animals = Animal.objects.all()
  return render(request, 'create_animal.html', {'animals': animals,'animal_form': animal_form})