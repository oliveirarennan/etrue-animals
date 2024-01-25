from django.db import models

# Create your models here.

class Animal(models.Model):
  name = models.CharField(max_length=100)
  species = models.ForeignKey('Species', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name}"


class Species(models.Model):
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f"{self.name}"