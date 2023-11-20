from django.db import models


class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.DecimalField(verbose_name="Valor",decimal_places=2,max_digits=6)

    def __str__(self):
        return self.localizacao