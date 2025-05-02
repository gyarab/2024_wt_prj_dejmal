from django.contrib import admin
from .models import *


@admin.register(GeneratorUser)
class GeneratorUserAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(EShop)
class EShopAdmin(admin.ModelAdmin):
    list_display = ("id", "creator")
    filter_horizontal = ("users",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "delivery_method", "delivery_location")
    filter_horizontal = ("items", "discount_programs")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    filter_horizontal = ("parameters", "subcategories", "items")

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "value_type")
    search_fields = ("name",)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    filter_horizontal = ("categories", "parameters")
    search_fields = ("name",)

@admin.register(EShopUser)
class EShopUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
    filter_horizontal = ("cart_items", "order_history", "active_discounts")
    search_fields = ("username",)

@admin.register(DiscountProgram)
class DiscountProgramAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "discount_percent")

@admin.register(DiscountProgramCondition)
class DiscountProgramConditionAdmin(admin.ModelAdmin):
    list_display = ("id", "discount_program", "min_total_price", "min_quantity")
    filter_horizontal = ("required_categories", "required_items")
# Register your models here.
