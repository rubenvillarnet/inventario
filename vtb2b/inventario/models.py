from django.db import models

# Create your models here.
class Articulo(models.Model):
    referencia = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.referencia
