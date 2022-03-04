from django.db import models


class Detalle(models.Model):
    cuenta_millonaria_dolares = models.FloatField()
    tipo_de_cambio = models.FloatField()
    cuenta_millonaria_soles = models.FloatField()
    cuenta_AFP_soles = models.FloatField()
    cuenta_ahorro_soles = models.FloatField()
    cuenta_sueldo_soles = models.FloatField()
    fecha = models.DateField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)