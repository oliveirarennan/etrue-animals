from django import forms
from .models import Animal, Species


class CreateSpecieForm(forms.ModelForm):
  name = forms.CharField(label='Nome', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'w-full text-zinc-900 rounded p-1 ml-2', 'placeholder': 'Nome da Espécie'}))
  class Meta:
    model = Species
    fields = ['name']


class CreateAnimalForm(forms.ModelForm):
  name = forms.CharField(label='Nome', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'w-full text-zinc-900 rounded p-1 ml-2', 'placeholder': 'Nome do animal'}))
  species = forms.ModelChoiceField(queryset=Species.objects.all(), label='Especie', empty_label='Selecione a espécie', required=True, widget=forms.Select(attrs={'class': 'w-full text-zinc-900 rounded p-1 ml-2', 'placeholder': 'Selecione a espécie'}))
  class Meta:
    model = Animal
    fields = ['name', 'species']