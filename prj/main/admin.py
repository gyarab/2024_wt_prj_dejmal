from django.contrib import admin
from .models import *

class EShopAdmin(admin.ModelAdmin):
    list_display = ["id"]

admin.site.register(EShop, EShopAdmin)

for model in modely:
    admin.site.register(globals[model])
# Register your models here.
