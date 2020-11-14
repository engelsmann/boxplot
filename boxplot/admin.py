from django.contrib import admin

from django.contrib import admin

# Register your models here.
from .models import Aflevering, AssesmentScore, Elev, Klasse
admin.site.register(Aflevering)
admin.site.register(AssesmentScore)
admin.site.register(Elev)
admin.site.register(Klasse)
