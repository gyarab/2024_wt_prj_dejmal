from django.db import models

__all__ = [
    "GeneratorUser",
    "EShop",
    "Order",
    "Category",
    "Parameter",
    "Item",
    "EShopUser",
    "modely"
]
modely = __all__[:-1]

# Uživatel generátoru
class GeneratorUser(models.Model):
    name = CharField(max_length=255, unique=True)
    password_hash = CharField(max_length=255)


# E-shop
class EShop(Model):
    creator = ForeignKey(GeneratorUser, on_delete=CASCADE)
    users = ManyToManyField(GeneratorUser, related_name="eshop_users")

# Objednávka z e-shopu
class Order(Model):
    user = ForeignKey(GeneratorUser, on_delete=CASCADE)
    items = ManyToManyField("Item")
    discount_programs = ManyToManyField("DiscountProgram", blank=True)
    delivery_method = CharField(max_length=255)
    delivery_location = CharField(max_length=255)

# Kategorie
class Category(Model):
    name = CharField(max_length=255)
    parameters = ManyToManyField("Parameter", blank=True)
    subcategories = ManyToManyField("self", symmetrical=False, related_name="parent_categories", blank=True)
    items = ManyToManyField("Item", blank=True)

# Parametr
class Parameter(Model):
    name = CharField(max_length=255)
    value_type = CharField(max_length=255)
    value = TextField()

# Položka (zboží)
class Item(Model):
    name = CharField(max_length=255)
    categories = ManyToManyField(Category)
    price = DecimalField(max_digits=10, decimal_places=2)
    quantity_discounts = TextField(null=True, blank=True)
    parameters = ManyToManyField(Parameter, blank=True)
    description = TextField()

# Uživatel e-shopu
class EShopUser(Model):
    username = CharField(max_length=255, unique=True)
    password_hash = CharField(max_length=255)
    cart_items = ManyToManyField(Item, blank=True)
    order_history = ManyToManyField(Order, blank=True)
    active_discounts = ManyToManyField("DiscountProgram", blank=True)
