from django.contrib import admin
from .models import *
models_list = [Kategorija, Aktivnost, Prijava]
# Register your models here.
admin.site.register(models_list)


