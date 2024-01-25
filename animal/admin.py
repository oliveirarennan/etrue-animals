from django.contrib import admin
from .models import Animal, Species
# Register your models here.
admin.site.register(Species)
admin.site.register(Animal)