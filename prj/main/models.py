from django.db import models

__all__ = [
    "GeneratorUser",
    "EShop",
    "Order",
    "Category",
    "Parameter",
    "Item",
    "EShopUser"
]

# Uživatel generátoru
class GeneratorUser(models.Model):
    name = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)


# E-shop
class EShop(models.Model):
    creator = models.ForeignKey(GeneratorUser, on_delete=models.CASCADE)
    users = models.ManyToManyField(GeneratorUser, related_name="eshop_users")

# Objednávka z e-shopu
class Order(models.Model):
    user = models.ForeignKey(GeneratorUser, on_delete=models.CASCADE)
    items = models.ManyToManyField("Item")
    discount_programs = models.ManyToManyField("DiscountProgram", blank=True)
    delivery_method = models.CharField(max_length=255)
    delivery_location = models.CharField(max_length=255)

# Kategorie
class Category(models.Model):
    name = models.CharField(max_length=255)
    parameters = models.ManyToManyField("Parameter", blank=True)
    subcategories = models.ManyToManyField("self", symmetrical=False, related_name="parent_categories", blank=True)
    items = models.ManyToManyField("Item", blank=True)

# Parametr
class Parameter(models.Model):
    name = models.CharField(max_length=255)
    value_type = models.CharField(max_length=255)
    value = models.TextField()

# Položka (zboží)
class Item(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_discounts = models.TextField(null=True, blank=True)
    parameters = models.ManyToManyField(Parameter, blank=True)
    description = models.TextField()

# Uživatel e-shopu
class EShopUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    cart_items = models.ManyToManyField(Item, blank=True)
    order_history = models.ManyToManyField(Order, blank=True)
    active_discounts = models.ManyToManyField("DiscountProgram", blank=True)
