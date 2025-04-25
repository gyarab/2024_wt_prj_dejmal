from django.contrib import admin
from .models import *

class Predek(admin.ModelAdmin):
    def __str__(self):
        return repr(self)
    def __repr__(self):
        string = "<" + type(self).__name__
        if hasattr(self, "_shown_attrs"):
            string += ":"
            for attr in self._shown_attrs:
                string += " " + attr + "=" + repr(getattr(self, attr))
        
        return string + ">"


@admin.register(GeneratorUser)
class GeneratorUserAdmin(Predek):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(EShop)
class EShopAdmin(Predek):
    list_display = ("id", "creator")
    filter_horizontal = ("users",)

@admin.register(Order)
class OrderAdmin(Predek):
    list_display = ("id", "user", "delivery_method", "delivery_location")
    filter_horizontal = ("items", "discount_programs")

@admin.register(Category)
class CategoryAdmin(Predek):
    list_display = ("id", "name")
    filter_horizontal = ("parameters", "subcategories", "items")

@admin.register(Parameter)
class ParameterAdmin(Predek):
    list_display = ("id", "name", "value_type")
    search_fields = ("name",)

@admin.register(Item)
class ItemAdmin(Predek):
    list_display = ("id", "name", "price")
    filter_horizontal = ("categories", "parameters")
    search_fields = ("name",)

@admin.register(EShopUser)
class EShopUserAdmin(Predek):
    list_display = ("id", "username")
    filter_horizontal = ("cart_items", "order_history", "active_discounts")
    search_fields = ("username",)

# Register your models here.
