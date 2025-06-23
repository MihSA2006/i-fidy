from django.contrib import admin
from .models import Arrondissement
from .models import Electeur

admin.site.register(Arrondissement)
admin.site.register(Electeur)