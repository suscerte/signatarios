from django.contrib import admin
from certificados.models import Certificado
from certificados.models import Signatario
from certificados.models import Estado

admin.site.register(Certificado)
admin.site.register(Signatario)
admin.site.register(Estado)
