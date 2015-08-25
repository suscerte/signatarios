from django.db import models

class Proveedor(models.Model):
        nombre = models.CharField(max_length = 1024)

        class Meta:
            verbose_name_plural = 'proveedores'

        def __unicode__(self):
                return self.nombre

