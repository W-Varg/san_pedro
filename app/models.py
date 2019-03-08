
from django.db import models

# Create your models here.

class Tarjeta(models.Model):
    number = models.CharField(max_length=20 ,unique=True)
    state = models.BooleanField(default=True)
    date_create = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_create']
    def __str__(self):
        return self.number


class Persona(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tarjetas = models.OneToOneField(Tarjeta, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class Registry(models.Model):
    tarjeta = models.CharField(max_length=20)
    user_name = models.ForeignKey(Persona, on_delete=models.CASCADE)
    date_registry = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.tarjeta
    

