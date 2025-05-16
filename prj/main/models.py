from django.db import models

__all__ = [
    "GeneratorUser",
    "EShop",
    "Order",
    "Category",
    "Parameter",
    "Item",
    "EShopUser",
    "DiscountProgram",
    "DiscountProgramCondition"
]


class Predek(models.Model):
    _show_id = True
    def __str__(self):
        return repr(self)
    def __repr__(self):
        string = "<" + type(self).__name__
        if hasattr(self, "_shown_attrs"):
            string += ":"
            
            if hasattr(self, "_show_id") and self._show_id:
                string += "id=" + repr(self.id)
            
            for attr in self._shown_attrs:
                string += " " + attr + "=" + repr(getattr(self, attr))
        
        return string + ">"


# Uživatel generátoru
class GeneratorUser(Predek):
    name = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    _shown_attrs = ("name",)

# E-shop
class EShop(Predek):
    creator = models.ForeignKey(GeneratorUser, on_delete=models.CASCADE)
    users = models.ManyToManyField(GeneratorUser, related_name="eshop_users")
    _shown_attrs = ("creator",)

# Objednávka z e-shopu
class Order(Predek):
    user = models.ForeignKey(GeneratorUser, on_delete=models.CASCADE)
    items = models.ManyToManyField("Item")
    discount_programs = models.ManyToManyField("DiscountProgram", blank=True)
    delivery_method = models.CharField(max_length=255)
    delivery_location = models.CharField(max_length=255)
    _shown_attrs = ("user",)

# Kategorie
class Category(Predek):
    name = models.CharField(max_length=255)
    parameters = models.ManyToManyField("Parameter", blank=True)
    subcategories = models.ManyToManyField("self", symmetrical=False, related_name="parent_categories", blank=True)
    items = models.ManyToManyField("Item", blank=True)
    _shown_attrs = ("name",)

# Parametr
class Parameter(Predek):
    name = models.CharField(max_length=255)
    value_type = models.CharField(max_length=255)
    value = models.TextField()
    _shown_attrs = ("name", "value_type", "value")

# Položka (zboží)
class Item(Predek):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_discounts = models.TextField(null=True, blank=True)
    parameters = models.ManyToManyField(Parameter, blank=True)
    description = models.TextField()
    _shown_attrs = ("name",)

# Uživatel e-shopu
class EShopUser(Predek):
    username = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    cart_items = models.ManyToManyField(Item, blank=True)
    order_history = models.ManyToManyField(Order, blank=True)
    active_discounts = models.ManyToManyField("DiscountProgram", blank=True)
    _shown_attrs = ("username",)

class DiscountProgramCondition(Predek):
    discount_program = models.ForeignKey('DiscountProgram', on_delete=models.CASCADE)
    min_total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    required_categories = models.ManyToManyField(Category, blank=True)
    required_items = models.ManyToManyField(Item, blank=True)
    min_quantity = models.PositiveIntegerField(blank=True)
    _shown_attrs = ("discount_program", "min_total_price", "required_categories", "required_items", "min_quantity")

class DiscountProgram(Predek):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    conditions = models.ForeignKey(DiscountProgramCondition, on_delete=models.CASCADE)
    _shown_attrs = ("name", "discount_percent")
